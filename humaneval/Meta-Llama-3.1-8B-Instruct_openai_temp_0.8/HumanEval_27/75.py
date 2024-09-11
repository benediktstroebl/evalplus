```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrld
```

In this code:

- We define the `flip_case` function that takes a string as input and returns the input string with all lowercase characters changed to uppercase and all uppercase characters changed to lowercase.

- The `swapcase()` method of the string class in Python is used to achieve this, which is a built-in method that swaps the case of the string.

- We test the function with example inputs and print the results.