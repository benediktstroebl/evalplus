```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base B"""
    assert isinstance(x, (int, float)), "Input must be a number"
    assert isinstance(base, int) and base > 0, "Base must be a positive integer"
    
    if base == 10:
        return str(x)
    
    result = ''
    while x > 0:
        whole = x // base
        remainder = x % base
        result = str(remainder) + result[::-1] if remainder != 0 else result
        x = whole
        base = base * 10
    
    return result
```