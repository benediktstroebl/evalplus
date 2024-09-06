Here's the Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. The `vowels` set stores all the uppercase vowels. The function then loops through the string at intervals of 2 indices using the `range(0, len(s), 2)` generator expression. It checks if the character at the current index is uppercase and a vowel, if so, it increments the count. Finally, it returns the total count.