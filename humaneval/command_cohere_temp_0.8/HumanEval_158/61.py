```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_word is None or char_count[word] > char_count[max_word]:
            max_word = word
    return max_word
```

The function uses a dictionary `char_count` to keep track of the number of unique characters for each word in the list. After iterating through all the words, it selects the word with the highest count of unique characters. If there are multiple words with the same highest count, it selects the first one in lexicographical order as specified in the problem statement. This solution is efficient with a time complexity of `O(n)` as it iterates over the list once, and performs constant-time operations for the set and dictionary lookups.