```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        unique = set(word)
        if not max_set or len(unique) > len(max_set):
            max_set = unique
            max_word = word
    return max_word
```

The function `find_max` accepts a list of strings, goes through each one, counts the unique characters in each word, and uses a handy `set` data structure to do so, as it automatically removes duplicate characters.

If the unique character count is larger than the previous maximum, it updates the maximum count and the corresponding word. Finally, if there is a tie in the number of unique characters, it uses the lexicographical order to pick the first one.