```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = max(a, b)
    if m % a == 0 or m % b == 0:
        return m

    return 1
```  This function determines the greatest common divisor of two numbers a and b. The function returns 1 if the maximum (m) is either equal to or divisible by both a and b.