### String Sequence Generator
#### Python Script

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The number up to which the sequence is generated.

    Returns:
        str: A string containing space-delimited numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage:
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```

This Python script defines a function `string_sequence` that generates a string containing space-delimited numbers from 0 to `n` (inclusive). The function uses a generator expression to create a sequence of numbers and the `join` method to concatenate them into a string.

The example usage at the end demonstrates how to use the `string_sequence` function with different inputs.