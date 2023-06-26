#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Spyder Editor

"""
import random

def generate_seed_phrase(word_list):
    seed_phrase = []
    while len(seed_phrase) < 12:
        word = random.choice(word_list)
        if word not in seed_phrase:
            seed_phrase.append(word)
    return ' '.join(seed_phrase)

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

def generate_seed_phrases(file_path, num_phrases):
    word_list = read_word_list(file_path)
    seed_phrases = set()
    while len(seed_phrases) < num_phrases:
        seed_phrase = generate_seed_phrase(word_list)
        seed_phrases.add(seed_phrase)
    return seed_phrases

# Example usage
file_path = r"C:\Users\Desktop\english.txt"
num_phrases = 40000
seed_phrases = generate_seed_phrases(file_path, num_phrases)
for phrase in seed_phrases:
    print(phrase)
    



