```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    total = 0
    vowels = 'AEIOU'
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            total += 1
    return total
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function checks if the character at the current index is uppercase and a vowel, and if so, it increments the total by 1. The function finally returns the total count of uppercase vowels in even indices. 

The example tests provided in the initial prompt return the following results:
```
1
0
0
``` 
You can test this script with other strings to verify its functionality further. In this case, the expected results are 1, 0, and 0 for the input strings 'aBCdEf', 'abcdefg', and 'dBBE', respectively.  This is consistent with the problem statement's intended behavior.