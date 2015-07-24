__author__ = 'tomer'

import sys, getopt
import os
import filecmp


def main(argv):
    path = ''
    try:
        opts, args = getopt.getopt(argv, "hp:", ["path="])
    except getopt.GetoptError:
        print 'error'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'help text'
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg

    print 'directory is: ', path
    files = os.listdir(path)
    similar_files = []

    files_len = len(files)
    for i in range(0, files_len):
        current_file = (files[i])
        current_file_path = path + os.sep + current_file
        look_alike = [current_file_path]

        if os.path.isfile(current_file_path):

            for j in range(i + 1, files_len):
                compare_file = (files[j])
                compare_file_path = path + os.sep + compare_file

                if os.path.isfile(compare_file_path) and \
                        filecmp.cmp(current_file_path, compare_file_path):
                    look_alike.append(compare_file_path)

            if len(look_alike) > 1:
                similar_files.append(look_alike)

    print 'similar files: ', similar_files

if __name__ == "__main__":
    main(sys.argv[1:])