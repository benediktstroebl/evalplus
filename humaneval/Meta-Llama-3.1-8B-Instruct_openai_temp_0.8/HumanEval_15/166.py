```markdown
### string_sequence function

This function generates a string containing space-delimited numbers starting from 0 up to n inclusive.

#### Code
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n (int): The upper limit of the sequence.

    Returns:
        str: A string containing space-delimited numbers.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))


# Test the function
if __name__ == "__main__":
    print(string_sequence(0))  # Output: '0'
    print(string_sequence(5))  # Output: '0 1 2 3 4 5'
    print(string_sequence(10))  # Output: '0 1 2 3 4 5 6 7 8 9 10'
```

#### Explanation

- This function uses the built-in `range()` function to generate a sequence of numbers from 0 up to `n` inclusive.
- The `map()` function is used to convert each number in the sequence to a string.
- The `' '.join()` method is then used to join these strings together with a single space in between each number.
- The function also includes docstrings for clarity and examples for testing purposes.
- In the test section, the function is called with different input values to demonstrate its usage.