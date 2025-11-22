# obtain a list of files in the input directory

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words

from ._internals.write_count_words import write_count_words


def main():

    input_folder = "data/input/"
    output_folder = "data/output/"

    ## read all lines
    all_lines = read_all_lines(input_folder)

    ### preprocess lines
    all_lines = preprocess_lines(all_lines)

    ### split in words
    words = split_into_words(all_lines)

    ### count words
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_files_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()


# create the directory output/ if it doesn't exist
# def write_count_words():
#     if not os.path.exists("data/output"):
#         os.makedirs("data/output")

#     # save the results using tsv format
#     with open("data/output/results.tsv", "w", encoding="utf-8") as f:
#         for key, value in counter.items():
#             # write the key and value to the file
#             f.write(f"{key}\t{value}\n")
