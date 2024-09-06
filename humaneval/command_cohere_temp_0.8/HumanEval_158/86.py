```python
def find_max(words):
    char_count = {}
    max_word = None
    max_word_idx = None
    for idx, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word.count(char) for char in unique_chars}
            max_word = word
            max_word_idx = idx
        elif num_unique_chars == len(char_count) and word < max_word:
            max_word = word
            max_word_idx = idx
    return max_word
```

The algorithm for the problem is:
1. Create an empty `char_count` dictionary.
2. Iterate over each word in the list.
3. For each word, extract unique characters and update the count of these characters in `char_count`.
4. If the number of unique characters is greater than the previous maximum, update `max_word` and its index.
5. If the number of unique characters is equal to the previous maximum, update `max_word` if the current word is lexicographically smaller.
6. Finally, return the maximum word.