# obtain a list of files in the input directory

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_in_words import split_in_words
from ._internals.write_count_words import write_count_words

def main():
    # mover a read_all_lines
    all_lines = read_all_lines()
    # mover a preprocess_lines
    all_lines = preprocess_lines(all_lines)
    # mover a split_in_words
    words = split_in_words(all_lines)
    # mover a count_words
    counter = count_words(words)
    # create the directory output/ if it doesn't exist
    write_count_words(counter)

if __name__ == "__main__":
    main()
