```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word for char, word in zip(unique_chars, [word])}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < char_count.values()[0]:
            max_char_word = word
    return max_char_word
```

The code defines a function `find_max` that solves the problem as described in the prompt. It iterates through each word in the input list and counts the unique characters, using a dictionary `char_count` to track the word associated with each unique character. If the current word has more unique characters than the previous maximum, it updates `char_count` and updates the `max_char_word`. If the word has the same number of unique characters but comes earlier in lexicographical order, it also updates the `max_char_word`. Finally, the function returns the `max_char_word`.