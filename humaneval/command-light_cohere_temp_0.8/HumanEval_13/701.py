```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0 or b == 0:
        return 0
    s = sorted((i for i in range(1, min(a, b) + 1))))
    return next(i for i in s if i * i <= a and i <= b)
```  This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b, it first handles edge cases where either of the inputs is zero and then raises a ValueError, and then it sorts the divisors of the larger number from smallest to largest up and returns the next divisor which satisfies the condition.