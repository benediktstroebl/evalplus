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
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All tests passed.")
```

This script defines the `strlen` function as specified and includes two test cases to verify its correctness. When run, the script checks the length of an empty string and a string containing 'abc', printing "All tests passed." if both tests succeed.