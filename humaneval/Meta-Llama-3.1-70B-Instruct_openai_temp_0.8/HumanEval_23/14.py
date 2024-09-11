```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3

def main():
    print("All test cases passed.")

if __name__ == "__main__":
    main()
```

This script defines a `strlen` function that takes a string as input and returns its length. It uses the built-in `len` function in Python, which returns the number of characters in a string.

The script includes two test cases to verify that the function behaves correctly. If the function works as expected, it prints "All test cases passed."