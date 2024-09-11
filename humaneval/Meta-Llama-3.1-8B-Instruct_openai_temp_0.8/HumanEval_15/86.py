```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The number up to which the sequence is generated.
    
    Returns:
        str: A string containing space-delimited numbers.
    
    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    # Use a generator expression to generate numbers from 0 to n (inclusive) and join them with spaces
    return''.join(map(str, range(n + 1)))
```
This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` (inclusive). It uses the `range` function to generate numbers from 0 to `n` and the `join` function to concatenate them into a string. The `map` function is used to convert the numbers to strings before joining them.