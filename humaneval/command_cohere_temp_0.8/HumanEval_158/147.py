```python
def find_max(words):
    words.sort()
    max_set = set()
    max_word = ""
    for word in words:
        curr_set = set(word)
        if len(curr_set) > len(max_set):
            max_set = curr_set
            max_word = word
    return max_word
```

The function `find_max` accepts a list of strings, sorts the list, and then iterates through the list to determine the word with the maximum number of unique characters. During each iteration, the function compares the set of characters present in the current word with the set of characters observed so far (stored in `max_set`). If the current set is larger in size, it replaces the previous set, as this indicates a maximum number of unique characters. The function returns the first word that has the maximum number of unique characters, consistent with the problem's requirements.