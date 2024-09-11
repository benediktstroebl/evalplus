```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string of space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This script defines a function `string_sequence` that generates a string sequence of numbers from 0 to `n` (inclusive) and returns it as a string of space-delimited numbers. The `join` method is used to concatenate the string representations of the numbers with spaces in between.

You can run this script directly in a Python environment, and it will print the results of the test cases. The test cases verify that the function behaves as expected for the inputs `0` and `5`.