```python
def greatest_common_divisor(a, b): 
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    if a > 0:
        return a
```  This function will return the greatest common divisor of the two numbers.