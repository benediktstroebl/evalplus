```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Example usage
print(flip_case('Hello'))  # Outputs: hELLO
print(flip_case('WORLD'))  # Outputs: worlD
```

In this script, the `flip_case` function uses a list comprehension to iterate over each character in the input string. The `swapcase()` method is used to swap the case of each character, effectively flipping the case of the entire string. Finally, the `join()` method is used to concatenate the characters back into a single string.