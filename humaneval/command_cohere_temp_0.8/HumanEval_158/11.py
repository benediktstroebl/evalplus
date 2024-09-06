```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        char_set = set(word)
        if char_set not in max_set or (char_set == max_set and word < max_word):
            max_set = char_set
            max_word = word
    return max_word
```

The function `find_max` operates on a list of strings, specifically looking for a word with the highest number of unique characters. Within the loop, each word is transformed into a set of characters, and these are compared against previous sets. If it finds a set that is equal or superior to the previous ones, or if it encounters a word that is lexicographically larger, it updates the max_set and max_word variables.

This algorithm ensures that it correctly identifies the word with the most unique characters and prioritizes words in lexicographical order when there is a tie.