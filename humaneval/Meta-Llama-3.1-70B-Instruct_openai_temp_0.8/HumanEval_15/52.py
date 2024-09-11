```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    Args:
    n (int): The end of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'
```

This Python function works by using the `range` function to generate a sequence of numbers from 0 to `n` (inclusive). The `map` function is then used to convert each number to a string. Finally, the `' '.join()` function is used to concatenate these strings into a single string, separated by spaces.