```markdown
### Solution: string_sequence function

The function `string_sequence` generates a string containing space-delimited numbers from 0 to `n` inclusive.

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.
    """
    return''.join(str(i) for i in range(n + 1))  # include n in the sequence

# Example use cases:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This solution uses a generator expression within the `join` method to efficiently generate the sequence of numbers as strings and join them with spaces.
```