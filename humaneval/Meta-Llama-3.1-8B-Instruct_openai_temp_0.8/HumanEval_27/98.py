```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Should print: hELLO
print(flip_case('WORLD'))  # Should print: wORLD
```

**How it works:**

- The `swapcase()` method of a string flips the case of each character in the string.
- The `''.join(...)` function is used to concatenate the characters back into a single string.
- We use a generator expression `(c.swapcase() for c in string)` to apply the `swapcase()` method to each character `c` in the string `string`.