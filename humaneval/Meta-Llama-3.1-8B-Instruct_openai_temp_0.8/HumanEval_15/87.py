```markdown
### String Sequence Generator

This script generates a string containing space-delimited numbers starting from 0 up to a given number `n` inclusive.

#### Code

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers from 0 to n inclusive.

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

#### Explanation

This script uses a generator expression to generate the sequence of numbers from 0 to `n` inclusive, and then uses the `join` method to concatenate these numbers into a string with spaces in between.

The `range(n + 1)` function generates numbers from 0 up to `n`, and the `str(i)` function converts each number to a string. The `join` method concatenates these strings with spaces in between, resulting in the desired output.

The example usage at the end demonstrates how to call the `string_sequence` function with different values of `n` and print the resulting strings.