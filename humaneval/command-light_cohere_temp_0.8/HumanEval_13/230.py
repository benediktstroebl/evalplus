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
```  This function determines the greatest common divisor of two integers a and b by employing a recursive approach. It examines the process to discover the GCD, checks for special cases, and recursively calls the function with the remainder and original divisor until the remainder equals 0.