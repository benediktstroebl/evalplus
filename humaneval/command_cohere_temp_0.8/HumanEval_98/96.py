Here's the Python code with a function that solves the problem:
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

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a list `vowels` to store the uppercase vowels and loops through the input string in increments of 2 to check for valid indices. Using the `isupper()` method and membership testing with `in`, it accurately computes the count of uppercase vowels in even positions, returning the result. 

Note: This solution assumes that the input string contains only uppercase letters and vowels. If the input may contain other characters, additional checks may be necessary.