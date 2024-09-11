### Python Script: string_sequence Function

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

This Python script defines a function `string_sequence(n)` that generates a string containing space-delimited numbers from 0 up to `n` inclusive. The function uses a generator expression within the `join()` method to create the desired string. The `range(n + 1)` function generates numbers from 0 up to `n` inclusive, and the `str(i)` function converts each number to a string. The `join()` method then concatenates these strings with a space in between each number.