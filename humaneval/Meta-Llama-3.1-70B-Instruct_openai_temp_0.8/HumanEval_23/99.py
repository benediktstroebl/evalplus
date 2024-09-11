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


# Test the function
if __name__ == "__main__":
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"

    print("All tests passed.")
```

To run this script, save it as a Python file (for example, `strlen.py`) and run it with Python (for example, `python strlen.py`). The script includes two test cases to verify that the `strlen` function works correctly. If the function works as expected, the script will print "All tests passed."