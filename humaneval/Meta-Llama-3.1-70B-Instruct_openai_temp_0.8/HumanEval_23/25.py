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
    print(strlen(''))  # Output: 0
    print(strlen('abc'))  # Output: 3
```
This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. It includes a docstring that provides documentation for the function, including example usage. The script also includes example usage at the end, which can be run by executing the script directly.