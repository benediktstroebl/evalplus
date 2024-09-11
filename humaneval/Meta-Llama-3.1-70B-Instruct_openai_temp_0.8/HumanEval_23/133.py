```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
    print("All test cases pass")
```

This script defines the `strlen` function as specified in the problem and includes test cases to verify its correctness. The test cases use Python's built-in `assert` statement to check if the function returns the expected values for the given inputs. If all test cases pass, it prints "All test cases pass".