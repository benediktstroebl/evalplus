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

This script defines a Python function `count_upper` that takes a string `s` as input and counts the number of uppercase vowels in even indices. It then returns the count. 

The example usage and test cases provided are correct and demonstrate the function's expected behavior. The function passes all the test cases and returns the correct counts for the provided examples, accordingly.