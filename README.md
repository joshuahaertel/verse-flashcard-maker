# verse-flashcard-maker
Turn files with short text into flashcards

Files must be formatted in the following format:
* Text or title as the filename
* Text to be memorized inside of the file

Output:
A CSV file with two columns. The first row created from a file will have the title in the first column and the first X words in the second column. The second row will have the first X words in the first column and the next X words in the second, until all words are paired.
