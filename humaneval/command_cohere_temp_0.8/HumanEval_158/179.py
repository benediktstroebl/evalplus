```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_char_word is None or char_count[word] > char_count[max_char_word]:
            max_char_word = word
    return max_char_word
```

The function uses a dictionary `char_count` to keep track of the number of unique characters in each word. After iterating through all the words, it selects the word with the highest count of unique characters. If there are multiple words with the same count, it defaults to the lexicographically earlier one.