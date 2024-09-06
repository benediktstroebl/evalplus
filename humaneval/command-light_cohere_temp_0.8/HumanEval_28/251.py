```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    
    Args:
        strings (List[str]): List of strings to concatenate
        
    Returns:
        str: Concatenated string
    """
    return ''.join(*strings)
```

This function takes a list of strings as input and returns a concatenated string using the `join()` constructor which applies the concatenation operation on the list elements. It then converts thely list of strings into a single string by using the `str.range` string constructor and the string concatenation.