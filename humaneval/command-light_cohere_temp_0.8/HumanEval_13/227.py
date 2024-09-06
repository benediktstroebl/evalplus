```python
def greatest_common_divisor(a, b): 
    while b != 0:
        rem = a % b
        a = b
        b = rem 
    if a > 0:
        return a
  return None
```