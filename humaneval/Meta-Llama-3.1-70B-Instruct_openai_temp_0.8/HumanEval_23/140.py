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
    # Test the function with example use cases
    print("Length of empty string: ", strlen(''))  # Expected output: 0
    print("Length of 'abc': ", strlen('abc'))  # Expected output: 3

if __name__ == "__main__":
    main()
```