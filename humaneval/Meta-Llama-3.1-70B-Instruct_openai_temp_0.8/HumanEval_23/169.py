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

# Example usage:
if __name__ == "__main__":
    print(strlen(''))  # Outputs: 0
    print(strlen('abc'))  # Outputs: 3
    print(strlen('hello world'))  # Outputs: 11
```