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

def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3

if __name__ == "__main__":
    test_strlen()
    print("All tests passed.")
```

This script defines the `strlen` function as requested and includes a `test_strlen` function to verify its correctness. The `if __name__ == "__main__":` block runs the tests when the script is executed directly. If all tests pass, it prints "All tests passed."