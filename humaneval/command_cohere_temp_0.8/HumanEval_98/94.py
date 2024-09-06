Here's the Python script with a function that solves the problem:
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
    count = sum(1 for i, char in enumerate(s, start=1) if i % 2 == 0 and char.isupper() and char in upper_vowels)
    return count
```
This script defines a function `count_upper()` that:
1. Receives a string as an input.
2. Retrieves the number of uppercase vowels in even indices of the string.
3. Tests if a character is an uppercase vowel using the `isupper()` and `in` functions.
4. Returns the count of uppercase vowels in even indices. 

The code uses a generator expression, which provides a convenient way to create a list of results and then sum them. The sum function in Python works with any iterable, making it versatile for different data structures.