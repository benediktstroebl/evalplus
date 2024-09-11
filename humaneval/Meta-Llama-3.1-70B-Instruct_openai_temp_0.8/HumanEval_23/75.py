```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    # Initialize a counter variable to 0
    length = 0
    
    # Iterate over each character in the string
    for _ in string:
        # Increment the counter for each character
        length += 1
    
    # Return the total length
    return length

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

However, it's worth noting that Python already has a built-in function `len()` to calculate the length of a string, so unless this is an exercise in implementing the `len()` function from scratch, you would typically use the built-in function instead:

```python
def strlen(string: str) -> int:
    return len(string)
```