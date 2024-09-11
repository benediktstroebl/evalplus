```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Example use cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, the `string_sequence` function takes an integer `n` as input and returns a string of space-delimited numbers from 0 to `n` inclusive. The `map(str, range(n + 1))` expression generates a sequence of strings representing the numbers from 0 to `n`, and the `join` method concatenates these strings with spaces in between. The `+ 1` in `range(n + 1)` is used to include `n` in the sequence.