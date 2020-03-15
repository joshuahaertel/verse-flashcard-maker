#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from typing import List


class FlashcardMaker:
    def __init__(self, output_file, input_files, chunk_size, prefix):
        self.output_file = output_file
        self.input_files = input_files  # type: List[str]
        self.chunk_size = chunk_size
        self.prefix = prefix

    def make(self):
        with open(self.output_file, 'w') as output_file:
            for input_file_name in self.input_files:
                with open(input_file_name, 'r') as input_file:
                    _, file_name = input_file_name.rsplit(os.sep, 1)
                    title, _ = file_name.rsplit('.', 1)
                    escaped_title = title.replace('"', '""')
                    front = f'{self.prefix}{escaped_title}'
                    word_lists = self.get_word_list(input_file)
                    for word_list in self.get_chunks(word_lists):
                        back = ' '.join(word_list)
                        formatted_back = back.replace('"', '""')
                        output_file.write(f'"{front}","{formatted_back}"\n')
                        front = formatted_back

    @staticmethod
    def get_word_list(input_file):
        input_file_text = input_file.read()
        input_file_text = input_file_text.strip()
        words = input_file_text.split()
        return words

    def get_chunks(self, word_lists):
        length_word_list = len(word_lists)
        for chunk_start in range(0, length_word_list, self.chunk_size):
            if chunk_start + self.chunk_size > length_word_list:
                chunk_end = length_word_list
            else:
                chunk_end = chunk_start + self.chunk_size
            yield word_lists[chunk_start:chunk_end]


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('output_file', help='CSV file to output to')
    arg_parser.add_argument('-chunk-size', type=int, default=5, help=(
        'How many words to show on each flashcard'
    ))
    arg_parser.add_argument('-prefix', default='', help=(
        'Prefix to add before the first card'
    ))
    arg_parser.add_argument('input_files', help='File to read in', nargs='*')
    args = arg_parser.parse_args()
    flashcard_maker = FlashcardMaker(
        args.output_file, args.input_files, args.chunk_size, args.prefix
    )
    flashcard_maker.make()
