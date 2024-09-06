```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """
    
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return '0'
    s = '0'
    while n > 0:
        s += str(n)
        n -= 1
    return s
```