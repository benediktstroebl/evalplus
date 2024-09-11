```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end of the sequence.

    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return''.join(map(str, range(n + 1)))

# Example use cases:
print(string_sequence(0))  # Outputs: 0
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```
This script uses the `join()` function to concatenate the numbers from 0 to `n` (inclusive) into a single string, with each number separated by a space. The `map()` function is used to convert each number to a string, as `join()` requires all elements to be strings. The `range(n + 1)` function generates numbers from 0 to `n` inclusive.