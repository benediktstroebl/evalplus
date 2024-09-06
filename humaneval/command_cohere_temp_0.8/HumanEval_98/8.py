```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = ["A", "E", "I", "O", "U"]
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```
This function counts the number of uppercase vowels present in even indices of the string. It achieves this by iterating through the string at intervals of 2 indices using a for loop. For each iteration, it checks if the character at the current index is an uppercase vowel. If it is, the count is incremented. The result is the total count of uppercase vowels in even indices of the string.