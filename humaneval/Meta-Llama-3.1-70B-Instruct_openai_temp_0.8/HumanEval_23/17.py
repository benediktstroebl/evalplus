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
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"

if __name__ == "__main__":
    test_strlen()
    print("All tests passed")
```

In this solution, we define the function `strlen` as specified in the problem statement. We use the built-in Python function `len` to get the length of the given string.

We also include a `test_strlen` function to verify that the `strlen` function behaves as expected. The `assert` statements check the return values of `strlen` for the specified inputs. If any of the assertions are false, an `AssertionError` will be raised, indicating that the test has failed.

The `if __name__ == "__main__"` line ensures that the tests are only run when the script is executed directly, not when it is imported as a module in another script.