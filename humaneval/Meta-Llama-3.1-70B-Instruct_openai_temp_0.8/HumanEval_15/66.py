```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        str: A string containing space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this script, we define a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n`. We use a generator expression to iterate over the range of numbers from 0 to `n` (inclusive), convert each number to a string, and then join these strings together with spaces in between using the `join` method.