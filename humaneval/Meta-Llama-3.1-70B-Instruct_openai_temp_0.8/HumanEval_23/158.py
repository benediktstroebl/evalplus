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
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass")
```

You can save this script to a file with a `.py` extension (e.g., `strlen.py`) and run it using Python (e.g., `python strlen.py`). The script defines the `strlen` function and includes two test cases using the `assert` statement. If the function works correctly, it will print "All test cases pass" when run.