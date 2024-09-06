```python
def greatest_common_divisor(a, b): 
    if not or not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input must be numbers")
  
    if a == 0 or b == 0:
        return 0
  
    m = a
    while b != 0:
        m, b = b, m % b 
    return m
```