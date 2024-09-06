```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set) or (len(char_set) == len(max_set) and word < max_word):
            max_set = char_set
            max_word = word
    return max_word
```

The `find_max` function iterates through each word in the input list and computes the unique characters within each word using a `set` and their count. It keeps track of the `set` with the most distinct characters and the corresponding word. If a new word has more unique characters or is equal in count and lexicographically less than the previous maximum, it updates the maximum values. Finally, the function returns the word with the most unique characters.