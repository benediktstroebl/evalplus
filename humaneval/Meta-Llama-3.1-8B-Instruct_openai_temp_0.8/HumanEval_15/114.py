### String Sequence Generator
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example usage
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
In this script, the `join()` function is used to concatenate the numbers into a string with spaces in between. The `map()` function applies the `str()` function to each number in the `range()` to ensure they can be concatenated into a string. The `range(n + 1)` generates numbers from 0 up to `n` inclusive.