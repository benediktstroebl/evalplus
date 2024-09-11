```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

Explanation:
- The `range(n + 1)` function generates numbers from 0 to `n` (inclusive).
- `map(str,...)` converts each number in the range to a string.
- `' '.join(...)` concatenates the strings with spaces in between.

This script defines the `string_sequence` function as per the given specification and includes example usage to demonstrate its functionality.