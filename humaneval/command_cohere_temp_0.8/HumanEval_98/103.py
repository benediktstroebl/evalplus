```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a string `upper_vowels` containing all uppercase vowels, then initializes a counter variable `count` to 0. It then loops through the characters of the input string in pairs, checking if the character is in `upper_vowels` and if it is at an even index. If both conditions are met, `count` is incremented. The function finally returns the total count.