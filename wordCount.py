import sys
import re


# Function to open a text file and return a map that contains the count of all the words in the text file
def read_input_file(file_name):
    # open file with given file name
    try:
        file = open(file_name, 'r')
        word_list = {}

        for line in file:
            line = line.lower()

            # Split words based on unneeded characters and strings
            words = re.split('[^a-zA-Z0-9]', line)
            words = filter(lambda x: x != "", words)

            for word in words:
                if word in word_list:
                    word_list[word] += 1
                else:
                    word_list[word] = 1

        file.close()
        return word_list

    except FileNotFoundError as err:
        print(err)
        return None


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 2 or len(args) == 0:
        raise Exception('Invalid arguments. Please include only 2 arguments. [input.txt, output.txt]')

    word_map = read_input_file(args[0])
    output = open(args[1], 'w')

    # Convert map to list for sorting
    sort_l = list(word_map.items())
    sort_l.sort()

    for pair in sort_l:
        output.write('{key} {count}\n'.format(key=pair[0], count=pair[1]))
    output.close()
