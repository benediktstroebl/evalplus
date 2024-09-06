Here's the Python script, including a function `count_upper()` that satisfies the given problem:
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

This function `count_upper()` takes a string `s` as its argument and calculates the count of uppercase vowels present in even indices of the string. It utilizes Python's built-in string `vowels` to identify valid vowels and iterates through the input string in intervals of two indices (i.e., even indices) to pinpoint and tally the uppercase vowels. 

The provided example usages within the function hint demonstrate its efficacy in solving the problem.