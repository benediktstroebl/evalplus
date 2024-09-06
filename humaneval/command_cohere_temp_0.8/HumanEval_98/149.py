```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    ans = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            ans += 1
    return ans
```

This script defines a Python function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It uses a for loop to iterate through the string, checking if each character is an uppercase vowel and whether it's located at an even index. It returns the count of uppercase vowels in even indices as the final result.