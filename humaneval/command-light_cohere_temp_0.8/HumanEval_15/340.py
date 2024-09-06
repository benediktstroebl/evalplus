```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 
    upto n inclusive. 
    
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(10)
    Traceback (most recent call last):
    ...
    ValueError: n must be non-negative integer
    """
    if not_negative(n):
        return ''.join(str(i) for i in range(n, 0, -1))
    else:
        raise ValueError('n must be non-negative integer')
    
def not_negative(n: int) -> bool:
    """Test function to check if n is negative"""
    return n < 0
```