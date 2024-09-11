```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
```

In this script:

- The `flip_case` function takes a string input and returns the string with case flipped.
- The `swapcase` method of each character in the string is used to flip the case. This method returns the lowercase version of an uppercase character and the uppercase version of a lowercase character.
- The `join` method is used to concatenate the characters back into a string.
- The script includes two test cases to demonstrate the function's usage.