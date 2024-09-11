### String Sequence Generator
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return''.join(map(str, range(n + 1)))

# Test cases
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```
This script defines a function `string_sequence(n)` that generates a string containing space-delimited numbers from 0 to `n` inclusive. The function uses the `join()` method to concatenate the numbers into a string, and the `map()` function to convert each number to a string before joining.

The test cases at the end of the script demonstrate the function's behavior for `n = 0` and `n = 5`.