```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    if n < 0:
        return "Error: n must be a positive integer"
    if n == 0 or n == 1:
        return '0'
    s = '0'
    while n > 0:
        n -= 1
        s += str(n)
    return s
```