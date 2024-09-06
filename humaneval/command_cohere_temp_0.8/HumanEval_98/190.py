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

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. The function returns the count of uppercase vowels in even indices of the string. The script passes the given tests: `count_upper('aBCdEf')` returns 1, `count_upper('abcdefg')` returns 0, and `count_upper('dBBE') returns 0`. 

The script's solution efficiently checks if the char at the current even index is uppercase and checks if it is a vowel, if so, it increments the count. The given solution has a time complexity of O(n/2), where n is the length of the given string, therefore, it is more efficient to iterate through half of the string at a time due to the even/odd check, it reduces the complexity to O(n) from O(n/2).