```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Invalid input"
    while a != 0:
        b = b % a
    return b
```  This function, `greatest_common_divisor`, calculates the greatest common divisor of two integers a and b.