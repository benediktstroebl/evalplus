### Length of a String

You can solve this problem by simply returning the `len()` of the string input. Here's a self-contained Python script:

```markdown
### strlen Function

```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
    string (str): The input string
    
    Returns:
    int: The length of the string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test strlen function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

You can save this script to a file (e.g., `strlen.py`) and run it using `python strlen.py` from the terminal. This will print the lengths of the empty string and the string `'abc'`. The `>>>` comments are examples of how you might use the `strlen` function in an interactive Python environment.