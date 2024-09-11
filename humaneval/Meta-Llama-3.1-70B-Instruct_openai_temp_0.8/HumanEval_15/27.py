```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers from 0 to n.
    """
    return''.join(str(i) for i in range(n + 1))


# Test cases
if __name__ == "__main__":
    print(string_sequence(0))   # Expected output: '0'
    print(string_sequence(5))   # Expected output: '0 1 2 3 4 5'
    print(string_sequence(10))  # Expected output: '0 1 2 3 4 5 6 7 8 9 10'
```

This script defines a function `string_sequence(n)` that uses a generator expression within the `join()` function to create a string of space-delimited numbers from 0 to `n`. The `range(n + 1)` generates numbers from 0 to `n` inclusive, and `str(i)` converts each number to a string. The `join()` function concatenates these strings with spaces in between. The script also includes test cases to verify the function's correctness.