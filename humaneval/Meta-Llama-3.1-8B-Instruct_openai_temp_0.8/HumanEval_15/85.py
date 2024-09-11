```markdown
### string_sequence Function

A Python function to generate a string containing space-delimited numbers
from 0 to n inclusive.

#### Code

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

#### Explanation

This function uses the `join` method to concatenate a list of strings with spaces in between.
The `map` function is used to convert integers to strings, and the `range` function generates numbers from 0 to n inclusive.

#### Example Usage

```python
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
```