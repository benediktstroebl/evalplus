```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
print(flip_case('HELLO WORLD'))  # Output: 'hELLO wORLD'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with all characters flipped from their original case. It uses a generator expression to iterate over each character in the input string, applies the `swapcase` method to each character (which swaps its case), and then joins the resulting characters back into a string using the `join` method. The function is then tested with a few example inputs to demonstrate its behavior.