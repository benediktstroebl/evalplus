### String Sequence Generator

The following Python script defines a function `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` inclusive.

```markdown
### Code
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))
```

### Usage

```markdown
# Example usage
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
The function uses the `join` method to concatenate the numbers in the sequence into a single string, with space characters in between each number. The `map` function is used to convert the numbers to strings before joining them, ensuring that the result is a string of space-delimited numbers.