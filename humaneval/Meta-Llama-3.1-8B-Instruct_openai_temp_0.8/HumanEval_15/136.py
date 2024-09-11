```markdown
### String Sequence Generator
#### Problem Statement
Generate a string containing space-delimited numbers starting from 0 up to n inclusive.

#### Solution

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
    return''.join(map(str, range(n + 1)))

# Example usage
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

#### Explanation
The `string_sequence` function uses the `join` method to concatenate a list of strings into a single string. The `map` function is used to convert each number in the range to a string, allowing them to be joined together. The `range` function generates numbers up to `n` inclusive, and we add 1 to `n` to include it in the sequence.
```