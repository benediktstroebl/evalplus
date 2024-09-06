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
    vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a list `vowels` containing all the uppercase vowels: 'AEIOU'. It then initializes a variable `count` to 0, which will keep track of the desired quantity. The function then loops through the characters of the input string `s` in pairs, checking if the character at even indices is uppercase and is a vowel. If it is, the count is incremented. Finally, the function returns the accumulated count.