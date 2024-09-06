```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 
    upto n inclusive.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return f"0 {n}{n+1} {n*n+1} {n*n+2}"
```  This function uses string formatting to create the desired sequence of numbers. It is tested for any name to make the function more readable and maintainable code.