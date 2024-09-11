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

def main():
    print("All test cases pass.")

if __name__ == "__main__":
    main()
```

This script defines the `strlen` function, which uses Python's built-in `len` function to return the length of the input string. It includes test cases to verify the function's correctness. When run, it prints "All test cases pass." if both test cases pass.