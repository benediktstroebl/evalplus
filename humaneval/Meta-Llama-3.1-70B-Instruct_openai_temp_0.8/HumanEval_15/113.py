```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))   # '0'
print(string_sequence(5))   # '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that uses the built-in `range` function to generate numbers from 0 up to `n` (inclusive) and the `map` function to convert these numbers to strings. The `' '.join(...)` expression is then used to concatenate these strings with spaces in between.

You can run this script and it will print the output of the test cases.