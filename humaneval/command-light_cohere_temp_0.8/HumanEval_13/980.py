```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is required")
    elif a == 0 or b == 0:
        return 0
    
    m = min(a, b)
    if m == 0:
        return 0
    
    # Finding the greatest divisor of the smaller number
    s = 0
    while a % s == 0 or b % s == 0:
        s += 1
    
    # Finding the highest common divisor
    # Note: a and b are now reversed to fit the algorithm
    a = 0
    while a <= m:
        b = 0
        while b <= m and a % b == 0:
            b += 1
        a = a + 1
    
    return min(a, b)
```