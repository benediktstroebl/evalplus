```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A space-delimited string of numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that uses a generator expression within the `join` method to create a space-delimited string of numbers from 0 to `n` (inclusive). The `range` function is used to generate the numbers, and `str(i)` is used to convert each number to a string. The `join` method concatenates these strings with a space in between each number. The example usage at the end demonstrates how to use the function.