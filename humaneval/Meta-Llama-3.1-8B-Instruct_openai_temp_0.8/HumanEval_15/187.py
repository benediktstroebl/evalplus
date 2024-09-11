```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(map(str, range(n + 1)))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script uses the built-in `range` function to generate a sequence of numbers from 0 to `n` (inclusive), and the `map` function to convert these numbers to strings. The `' '.join(...)` expression then concatenates these strings together with spaces in between, producing the desired output.