```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in zip(unique_chars, word)}
        elif len(unique_chars) == len(char_count):
            for char in unique_chars:
                if char not in char_count:
                    char_count = {char: word for word, char in zip(unique_chars, word)}
                    break
        if max_word is None or (len(char_count) > len(set(max_word)) and max_word < word):
            max_word = word
    return max_word
```

The `find_max` function takes a list of words as input and uses a dictionary to count the number of unique characters in each word. If a word has more unique characters than any previous word, it becomes the new candidate for the maximum. If a word has an equal number of unique characters but appears earlier in lexicographical order, it becomes the new candidate. The function returns the maximum word according to these criteria.