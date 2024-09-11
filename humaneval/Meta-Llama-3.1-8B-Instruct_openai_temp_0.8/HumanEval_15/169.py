```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

In this code:

- The `range(n + 1)` function generates a sequence of numbers from 0 to `n` inclusive.
- The `map(str,...)` function converts each number in the sequence to a string.
- The `' '.join(...)` function joins these strings together with spaces in between, resulting in the desired output string.

This script not only defines the `string_sequence` function but also includes test cases to verify its correctness.