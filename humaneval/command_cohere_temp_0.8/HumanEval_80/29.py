```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
        if letters_count[letter] == 3:
            letters_count[letter] = 0  # To reset the counter for the next triplet
    return all(count <= 1 for count in letters_count)
```

The function `is_happy()` checks if the given string is happy by ensuring that its length is at least 3 and every 3 consecutive letters are distinct. This is done using a counter for each letter that resets after each triplet. The function returns `True` if all triplet counters are 0 or 1, otherwise, it returns `False`.