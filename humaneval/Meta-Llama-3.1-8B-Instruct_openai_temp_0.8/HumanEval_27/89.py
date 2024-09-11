### Case Flipper Script
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('Python'))  # Output: 'pYTHON'
```
This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The `swapcase()` method of each character in the string is used for this purpose. The example usage at the end demonstrates how to use this function.