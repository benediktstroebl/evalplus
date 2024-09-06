Here's the Python code with a function to achieve the specified task:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    vowels = 'AEIOU'
    count = 0
    length = len(s)
    if length % 2 == 0:
        for i in range(length):
            if s[i] in vowels and s[i].isupper() and (i + 1) % 2 == 0:
                count += 1
    return count
```

This function `count_upper()` takes a string `s` as its argument and calculates the count of uppercase vowels present in even indices of the string. It uses a list `vowels` to store the uppercase vowels and loops through the string, checking for valid characters and counting if they are in even indices. The comment section provides examples for better understanding.