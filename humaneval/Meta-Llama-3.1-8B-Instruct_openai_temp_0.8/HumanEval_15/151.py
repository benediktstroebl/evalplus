### Python Script to Generate String Sequence

```markdown
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))


# Test the function
print(string_sequence(0))
print(string_sequence(5))
```
```

In this script, we define a function `string_sequence` that uses the `join` method and `map` function to generate the desired string. The `range` function generates numbers from 0 to `n` inclusive, and `map` applies the `str` function to convert these numbers to strings. Finally, `join` concatenates these strings with spaces in between.

When you run this script, it will print the desired string sequences for the test cases `string_sequence(0)` and `string_sequence(5)`.