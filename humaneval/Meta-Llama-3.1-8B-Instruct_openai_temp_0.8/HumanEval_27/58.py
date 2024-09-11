Here's a Python script that meets the requirements:
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
```
In this script, the `flip_case` function uses a generator expression to iterate over each character `c` in the input string `string`. The `swapcase` method is used to flip the case of each character, and the resulting characters are then joined back together into a single string with `''.join()`. The example usage demonstrates how to call the `flip_case` function with different inputs and print the results.