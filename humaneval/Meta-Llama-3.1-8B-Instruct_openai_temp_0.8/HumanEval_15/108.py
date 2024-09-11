```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script uses a list comprehension and the `join` method to create a string containing the numbers from 0 to `n` inclusive, separated by spaces. The `range` function generates numbers from 0 to `n`, and the `str` function converts each number to a string. The `join` method then concatenates these strings with spaces in between.