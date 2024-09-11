```markdown
### Problem: Generate a string sequence of space-delimited numbers
#### Solution: Python script to solve the problem

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string of space-delimited numbers from 0 to n.

    Example:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(i) for i in range(n + 1))


# Test the function
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

### Explanation
- This Python script defines a function `string_sequence(n)` that generates a string sequence of space-delimited numbers from 0 to n (inclusive).
- The function uses a generator expression to generate numbers from 0 to n and joins them into a string with spaces in between using `' '.join()`.
- The script includes example usage and a docstring to explain the function's behavior.
```