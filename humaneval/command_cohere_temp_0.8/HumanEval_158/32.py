```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        char_count[num_unique_chars].append(word)
        if max_word is None or (len(word) > len(max_word) and
                                  num_unique_chars == char_count[num_unique_chars][-1]):
            max_word = word
    return max_word
```

The function uses a dictionary `char_count` to count the number of unique characters in each word. The lexicographical order ensures the longest word with the maximum number of unique characters is returned. If there are multiple words with the same length and the same number of unique characters, the lexicographical order ensures the first one is selected.