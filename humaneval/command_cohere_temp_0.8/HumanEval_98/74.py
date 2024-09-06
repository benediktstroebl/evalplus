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

This code defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It utilizes a list `vowels` to store the uppercase vowels: 'AEIOU'. The code then loops through the string `s` in increments of 2 using the `range()` function, checks if the character at that index is uppercase using the `isupper()` method, and checks if the character is in the `vowels` list using the `in` operator. If both conditions are met, it increments the count variable. Finally, the function returns the calculated count.