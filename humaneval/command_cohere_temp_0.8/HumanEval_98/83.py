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
    # Using list comprehension to check if the character at even indices are uppercase vowels
    even = [char for i, char in enumerate(s) if i % 2 == 0 and char.isupper() and char in 'AEIOU']
    return len(even)
```

This script provides a function that solves the problem using a list comprehension, enumerating through characters, and checking for uppercase vowels in even indices of the string.

The `count_upper()` function takes a string as input and returns the number of uppercase vowels in even indices of the string. 

The example usage provided in the docstring gives the following result:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
```

This solution is efficient and does not require any additional modules beyond the Python standard library, making it suitable for any Python environment.