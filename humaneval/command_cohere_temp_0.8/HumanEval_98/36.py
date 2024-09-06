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

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a list `upper_vowels` containing all uppercase vowels, then initializes a counter `count` to 0. It then iterates through the characters of the input string in steps of 2 (i.e., even indices), and increments the count whenever an uppercase vowel is encountered. Finally, the function returns the calculated count.