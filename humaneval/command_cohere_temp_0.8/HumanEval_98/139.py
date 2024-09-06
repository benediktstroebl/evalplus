Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the prompt:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```

This function uses a set called `upper_vowels` to efficiently check whether the character at a given index is an uppercase vowel. The function iterates through the string `s`, examining each character at every second index (i.e., even indices) and incrementing the count if the character is an uppercase vowel. The result is the count of uppercase vowels in even indices of the string.

The function's docstring also provides example cases, which the script's function should accurately solve. 

This code should be contained in a single Python script file, and it can be run as is without any dependencies or external modules.