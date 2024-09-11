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


# Example usage:
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10))  # Output: 0 1 2 3 4 5 6 7 8 9 10
```
This script defines the `string_sequence` function, which generates the desired string by using a generator expression to iterate over the numbers from 0 to `n` (inclusive), converting each number to a string, and then joining them together with spaces in between. The `join` method of the `str` type is used for this purpose. The example usage demonstrates how to call this function with different values of `n`.