```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass.")
```

To run this script, simply copy and paste it into a Python file (e.g., `strlen.py`) and execute it using Python (e.g., `python strlen.py`). The script defines a function `strlen` that calculates the length of a given string and includes two test cases to verify its correctness. If the test cases pass, it prints "All test cases pass." to the console.