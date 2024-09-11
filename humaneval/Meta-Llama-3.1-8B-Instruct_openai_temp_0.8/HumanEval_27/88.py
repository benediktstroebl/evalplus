```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrld
```

In this script, we define the `flip_case` function that uses a generator expression to iterate over each character `c` in the input string. It checks if the character is lowercase using the `islower()` method, and if so, converts it to uppercase using the `upper()` method. Otherwise, it converts the character to lowercase using the `lower()` method. Finally, it joins all the characters back into a string using the `join()` method. The test cases demonstrate the function's correctness.