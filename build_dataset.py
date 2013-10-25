# -*- coding: utf-8 -*-
__author__ = 'klb3713'

import os
import sys
import re
import config
import vocabulary

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

p_word = re.compile(r'[a-zA-Z0-9]+')


def getNormalWord(word):
    if word.isdigit():
        return config.SYMBOL_WORD
    elif word.isalnum():
        return word.lower()

    word = ''.join(p_word.findall(word))
    if word.isdigit():
        return config.SYMBOL_WORD
    else:
        return word.lower()


def build_vocabulary():
    if not os.path.exists(config.TRAIN_FILE):
        print("Error: can't find train file '%s'!" % config.TRAIN_FILE)
        exit()
    train_size = 0
    with open(config.TRAIN_FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            words = line.split()
            for word in words:
                word = getNormalWord(word)
                if word:
                    train_size += 1
                    vocabulary.add(word)

    print("TRAIN SIZE: %d" % train_size)
    print("VOCABULARY SIZE: %d" % vocabulary.length())
    vocabulary.dump_vocabulary()

def build_samples():
    pass


if __name__ == "__main__":
    build_vocabulary()