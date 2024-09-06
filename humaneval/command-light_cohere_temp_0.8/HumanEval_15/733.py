```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> print(string_sequence(0)) 
    '0'
    >>> print(string_sequence(5)) 
    '0 1 2 3 4 5'
    >>> print(string_sequence(10)) 
    '0 9 8 7 6 5'
    >>> print(string_sequence(100)) 
    '0 99 98 97 96 95'
    """
    return f"0 {n}{' '}"
```