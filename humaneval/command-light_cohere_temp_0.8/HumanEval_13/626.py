```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided.")
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    m = min(a, b)
    for d in range(1, int(m**0.5) + 1):
        if a % d == 0 and b % d == 0:
            return d
    return -1
``` 
This code defines a function `greatest_common_divisor(a, b)` that returns the greatest common divisor of two integers `a` and `b`. The function performs several checks to ensure that both inputs are valid numbers and that they are not both zero, and then iterates through all divisors of the number `m`, which is the smaller of the two input numbers, and returns the greatest common divisor found during the loop.