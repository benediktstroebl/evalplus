```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass.")
```
This script defines a `strlen` function that returns the length of a given string. It uses Python's built-in `len` function to calculate the length of the string. The script also includes test cases to verify the correctness of the `strlen` function. If all test cases pass, it prints "All test cases pass."