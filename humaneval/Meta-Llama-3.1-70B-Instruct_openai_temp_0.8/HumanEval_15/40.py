### String Sequence Function

The following Python function generates a string sequence of numbers from 0 up to `n` inclusive, separated by spaces.

```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence.

    Returns:
    str: A string containing the sequence of numbers.
    """
    return''.join(str(i) for i in range(n + 1))

# Example usage
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
```

In this script:

1.  We define the `string_sequence` function with an integer parameter `n`.
2.  Inside the function, we use a generator expression to generate numbers from 0 to `n` using the `range` function.
3.  We convert each number to a string using the `str` function.
4.  We use the `join` method to concatenate the string numbers with spaces in between.
5.  Finally, we provide example usage of the function to demonstrate its output.