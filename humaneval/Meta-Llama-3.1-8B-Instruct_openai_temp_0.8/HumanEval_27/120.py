```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.
    """
    return ''.join(c.swapcase() for c in string)

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
```

In this code:

*   We define the `flip_case` function that takes a string as input and returns the string with case flipped.
*   Inside the function, we use a generator expression to iterate over each character `c` in the string.
*   We use the `swapcase()` method to flip the case of each character and join the resulting characters back into a string using the `join()` method.
*   Finally, we provide an example usage of the `flip_case` function.