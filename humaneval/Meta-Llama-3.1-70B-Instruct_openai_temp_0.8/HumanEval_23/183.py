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

# Example usage
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
```