```markdown
### strlen Function
#### Returns the length of a given string

```python
def strlen(string: str) -> int:
    """
    Args:
    string (str): The input string

    Returns:
    int: The length of the input string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

#### Usage
You can use this function to get the length of any string. For example:

```python
print(strlen("Hello, World!"))  # Outputs: 13
print(strlen("Python"))  # Outputs: 6
```