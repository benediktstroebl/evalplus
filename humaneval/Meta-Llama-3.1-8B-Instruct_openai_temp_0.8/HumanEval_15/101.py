```markdown
**String Sequence Generation**
=====================================

This script generates a string of space-delimited numbers starting from 0 up to a given number `n` inclusive.

**Code**
--------

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        str: A string of space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

**Explanation**
---------------

This script uses a generator expression to generate numbers from 0 to `n` (inclusive) and joins them into a string with spaces in between using the `join()` method. The `range(n + 1)` function generates numbers from 0 to `n` inclusive, and the `str()` function is used to convert the numbers to strings.
```