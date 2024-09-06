```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function checks if the character is an uppercase vowel (`"AEIOU"`) and if it is in an even index, incrementing the count accordingly. The example provided in the problem statement would return 1, as there is one uppercase vowel 'E' in an even index. The provided tests ensure the functionality of the script.