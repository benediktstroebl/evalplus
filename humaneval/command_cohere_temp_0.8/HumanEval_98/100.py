```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    uppercase_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count
```
This function uses a set called `uppercase_vowels` to efficiently check whether the current character is an uppercase vowel or not. The loop iterates over the string's characters in increments of 2, checking for instances where the character is an uppercase vowel. The `count` variable is increased for each such occurrence. The function returns the total count of uppercase vowels found in even indices.