### Python Script to Generate String Sequence

```python
def string_sequence(n: int) -> str:
    """
    Returns a string containing space-delimited numbers from 0 to n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))


# Example usage
if __name__ == "__main__":
    print(string_sequence(0))   # Output: '0'
    print(string_sequence(5))   # Output: '0 1 2 3 4 5'
    print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script uses a generator expression within the `str.join()` method to create the desired string sequence. The expression `range(n + 1)` generates numbers from 0 to `n` inclusive, and `str(i)` converts each number to a string before joining them with spaces in between.