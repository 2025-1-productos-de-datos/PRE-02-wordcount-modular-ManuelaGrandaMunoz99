# obtain a list of files in the input directory
import os

from .write_count_words import write_count_words

def read_all_lines():
    all_lines = []
    files_in_input_dir=os.listdir('data/input/')
    for filename in files_in_input_dir:
        with open(filename,"r",encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines

def main():
    files_in_input_dir=os.listdir('data/input/')
    #all_lines = read_all_lines()
    # count the frequency of the words in the files in the input directory
    counter={}
    for filename in files_in_input_dir:
        with open('data/input/'+filename) as f:
            for l in f:
                for w in l.split( ):
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_count_words(counter)

if __name__ == "__main__":
    main()
