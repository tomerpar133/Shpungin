__author__ = 'Avihay'

import os


def organize_files(file_groups, out_dir):
    for group in file_groups:
        for file in group:
            filename, file_extension = os.path.splitext(file)
            if not os.path.isdir(os.path.join(out_dir, file_extension)):
                os.mkdir(os.path.join(out_dir, file_extension))
            os.rename(file, os.path.join(out_dir, filename, file_extension))
