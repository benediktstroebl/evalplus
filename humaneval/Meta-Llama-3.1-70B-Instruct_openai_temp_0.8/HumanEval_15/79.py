```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    # Use a generator expression to generate the numbers from 0 to n
    numbers = (str(i) for i in range(n + 1))
    
    # Join the numbers into a string with spaces in between
    sequence =''.join(numbers)
    
    return sequence

# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

Alternatively, you can also achieve this using the `map` and `join` functions in a one-liner:

```python
def string_sequence(n: int) -> str:
    return''.join(map(str, range(n + 1)))
```