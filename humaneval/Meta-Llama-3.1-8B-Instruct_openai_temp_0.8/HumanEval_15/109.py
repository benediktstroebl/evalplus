```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The end number of the sequence.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Test cases
if __name__ == "__main__":
    print(string_sequence(0))
    print(string_sequence(5))
```

This script defines the `string_sequence` function, which uses a generator expression to generate numbers from 0 to `n` (inclusive) and then uses the `join` method to concatenate them into a string with spaces in between. The test cases at the end of the script demonstrate how the function works.