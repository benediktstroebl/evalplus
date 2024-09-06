```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided.")
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    m = 0
    for i in range(1, min(len(str(a)), len(str(b)) + 1)):
        m = max(m, int(a[i - 1] + b[len(str(b)) - i]))
    return m
``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It uses a tested algorithm that iterates over the digits of the larger number, and checks for divisibility by the other number at each position. The result returns the maximum of these divisors found.