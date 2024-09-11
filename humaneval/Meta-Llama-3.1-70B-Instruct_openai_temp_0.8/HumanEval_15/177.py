```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))

# Example use cases:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
This script uses a generator expression within the `join` method to generate the sequence of numbers and convert them to strings. The `join` method then concatenates these strings with spaces in between. The `range` function generates numbers from 0 up to `n` inclusive by passing `n + 1` as the upper limit.