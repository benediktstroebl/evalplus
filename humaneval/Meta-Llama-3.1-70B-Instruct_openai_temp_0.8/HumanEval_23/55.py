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

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function is a built-in Python function that returns the number of items in an object. When the object is a string, it returns the number of characters in the string.

The test cases are written using the `assert` statement, which checks if the condition is true. If the condition is false, it raises an AssertionError. 

If all test cases pass, it prints "All test cases pass."