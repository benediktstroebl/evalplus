Here's a Python script with a function that solves the problem:
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

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a set of all uppercase vowels, then iterates through the string s in steps of 2 (i.e., even indices), and checks each character at these indices. If it finds a character that is an uppercase vowel, it adds 1 to the count. Finally, the function returns the accumulated count.