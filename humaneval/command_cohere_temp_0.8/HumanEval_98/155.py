Here's the Python code to solve the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This code defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It uses a list `vowels` to store the uppercase vowels: 'AEIOU'. The code then loops through the string `s` in increments of 2 using the `range(0, len(s), 2)` and checks if the character at that index is uppercase and a vowel, if so, it increments the count. Finally, it returns the computed count.