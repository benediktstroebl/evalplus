```markdown
### Python Script to Generate String Sequence
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Example:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))

# Test the function
print(string_sequence(0))
print(string_sequence(5))
```
This script defines the `string_sequence` function, which uses a generator expression to generate numbers from 0 to `n` (inclusive) and then joins them into a space-delimited string using `' '.join()`. The function is then tested with `print` statements.