Here's the Python script with a function that solves the problem:
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
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```
This function counts the number of uppercase vowels in even indices of the given string `s`. It uses a list `upper_vowels` to store the uppercase vowels and iterates through the string in steps of 2, checking each character at even indices to see if it belongs to the `upper_vowels` list. If it does, it increments the count. Finally, it returns the computed count.