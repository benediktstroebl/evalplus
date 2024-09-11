```markdown
### strlen Function
#### A Simple Function to Calculate the Length of a Given String

```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): The input string for which the length needs to be calculated.

    Returns:
    int: The length of the given string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

#### Usage
You can use the `strlen` function to calculate the length of any given string.

```python
print(strlen('Hello, World!'))  # Output: 13
print(strlen('Python'))  # Output: 6
```
This `strlen` function simply uses Python's built-in `len` function, which returns the number of items in an object. In the case of strings, this is equivalent to the number of characters in the string.