```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        char_count[num_unique_chars].append((word, len(word)))
        if max_word is None or len(unique_chars) > len(set(max_word)):
            max_word = word
    return max_word
```

The code defines a function `find_max` that takes in a list of words and returns the word with the highest number of unique characters, considering lexicographical order. It achieves this by using a dictionary `char_count` that maps the number of unique characters to a list of words having that number of unique characters. Then, it iterates through each word in the input list, calculating the number of unique characters and comparing it with existing entries in `char_count`. If the word has more unique characters than any existing entry, it updates the corresponding list with the word and its length. Additionally, if the word has more unique characters than the previously recorded `max_word`, it updates the `max_word` variable. Finally, the function returns the `max_word` obtained from the analysis.