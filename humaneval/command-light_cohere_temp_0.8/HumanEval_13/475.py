```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b%a, a) + 1
```  This function calculates the greatest common divisor of two integers a and b, returning the result.