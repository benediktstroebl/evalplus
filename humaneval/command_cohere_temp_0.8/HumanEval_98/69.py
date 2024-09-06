```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    uppercase_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The set `uppercase_vowels` stores all the uppercase vowels. The function then iterates through the string at intervals of 2 indices using a for loop. It checks if the character at the current index is in the set of uppercase vowels, and if so, it increments the count. Finally, the function returns the total count of uppercase vowels in even indices.