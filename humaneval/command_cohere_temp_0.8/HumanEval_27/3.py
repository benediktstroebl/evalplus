```python
def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Shifts uppercase characters to lowercase and vice versa.
    
    Args:
    - string (str): Input string to modify
    
    Returns:
    - str: Modified string with flipped case
    
    Example:
    >>> flip_case('Hello World')
    'hELLO WORLD'
    """
    return string.swapcase()
```
This function utilizes the `swapcase` method, which is directly built into Python strings (strings are objects in Python, capitalized as `str`). This method conveniently switches the case of characters, hence achieving the desired result.

The script includes an example and returns the statement immediately below to showcase how this function works:
```python
>>> flip_case('Hello World')
'hELLO WORLD'
```