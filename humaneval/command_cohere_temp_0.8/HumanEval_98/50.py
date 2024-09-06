```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Using list and subtracting final length by 2 to only consider every second index
    even = [i for i, char in enumerate(s) if char.isupper() and char in 'AEIOU' and i % 2 == 0]
    return len(even)
```

The solution leverages the list comprehension and enumerate functions to iterate through each character in the string `s`. It filters characters based on the following conditions:
1. The character is in uppercase (using the `isupper()` method).
2. The character is a vowel (using the condition `char in 'AEIOU'`).
3. The character's index is even (i.e., it's located at an even index), determined using the modulo operator `% 2 == 0`.

Subtracting `len(even)` by 2 ensures that we account only for every second index. Ultimately, the length of the resulting even list indicates the number of uppercase vowels in even positions, according to the given problem's specifications.