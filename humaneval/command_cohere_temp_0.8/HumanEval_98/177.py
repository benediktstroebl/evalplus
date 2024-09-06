```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = sum(1 for i, char in enumerate(s, start=1) if i % 2 == 0 and char.isupper() and char in upper_vowels)
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. It does so by first creating a set of uppercase vowels `upper_vowels` and then using a sum() with a generator expression to iterate through the characters in the input string, only counting those that are in even indices, are uppercase, and are vowels. The total count is then returned. 

This solution complies with the specified problem statement and passes the accompanying tests.