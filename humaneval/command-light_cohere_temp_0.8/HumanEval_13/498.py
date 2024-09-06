```python
def greatest_common_divisor(a, b): 
    if not or not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input types. Ensure both a smoketh integers.")
    
    m = min(a, b)
    while m % a != 0 and m % b != 0: 
        m += 1
    
    return m
```