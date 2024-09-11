```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers from 0 to n inclusive.
    """
    return''.join(map(str, range(n + 1)))  # +1 to include n in the sequence


# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script uses the built-in `join()` function in combination with a generator expression (`range(n + 1)`) to create the desired string. The `map()` function is used to convert the integers to strings before joining them into a single string. The `+1` is necessary to include `n` in the sequence.