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
    print files
    similar_files = []

    # for file_info in files:
    #
    #     print os.path.abspath(file_info)

    files_len = len(files)
    for i in range(0, files_len):
        current_file = os.path.abspath(files[i])
        print 'checking file ', current_file

        look_alike = [current_file]

        print '\t is path ', os.path.isfile(current_file)

        if os.path.isfile(current_file):

            for j in range(i, files_len):
                compare_file = os.path.abspath(files[j])

                if os.path.isfile(compare_file) and filecmp.cmp(current_file, compare_file):
                    look_alike.append(compare_file)

            if len(look_alike) > 1:
                similar_files.append(look_alike)

    print 'similar files: ', similar_files

if __name__ == "__main__":
    main(sys.argv[1:])