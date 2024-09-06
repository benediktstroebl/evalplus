Here's the Python script, including a self-contained function `count_upper` that solves the problem as outlined in the prompt:
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
This function takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It utilizes a list `vowels` to store the uppercase vowels: 'AEIOU'. The function then iterates through the string in increments of 2 using the `range` function, checking for uppercase vowels in even indices and incrementing a counter. The result is the total count of uppercase vowels in even indices.