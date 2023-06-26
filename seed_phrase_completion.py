#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

def find_missing_words(seed_phrase, word_list):
    seed_words = seed_phrase.split()
    missing_words = []
    for word in seed_words:
        if word not in word_list:
            missing_words.append(word)
    return missing_words

def find_possible_combinations(seed_phrase, word_list):
    seed_words = seed_phrase.split()
    possible_combinations = []
    missing_words = find_missing_words(seed_phrase, word_list)
    for r in range(1, len(missing_words) + 1):
        for combination in itertools.combinations(word_list, r):
            filled_seed_phrase = seed_phrase
            for i in range(len(missing_words)):
                filled_seed_phrase = filled_seed_phrase.replace(missing_words[i], combination[i])
            possible_combinations.append(filled_seed_phrase)
    return possible_combinations

# Example usage
file_path = r"C:\Users\Desktop\english.txt"
seed_phrase = input("Enter the incomplete seed phrase: ")
word_list = read_word_list(file_path)
missing_words = find_missing_words(seed_phrase, word_list)
if len(seed_phrase.split()) not in [24, 18, 12]:
    print("Invalid seed phrase length. Please enter a 24-, 18-, or 12-word seed phrase.")
elif missing_words:
    print("Missing words:")
    for word in missing_words:
        print(word)
    possible_combinations = find_possible_combinations(seed_phrase, word_list)
    print("\nPossible combinations:")
    for combination in possible_combinations:
        print(combination)
else:
    print("All words are present in the seed phrase.")

