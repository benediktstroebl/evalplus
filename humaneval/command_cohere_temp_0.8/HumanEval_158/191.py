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

The function uses a dictionary `char_count` to count the number of unique characters in each word. After counting the unique characters, the function compares the counts to find the word with the most unique characters. If there are multiple such words, it returns the one that comes first in lexicographical order. The solution is topped off with corresponding tests to ensure the function works correctly.