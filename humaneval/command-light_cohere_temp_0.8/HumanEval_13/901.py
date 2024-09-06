```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Two numbers must be provided.")
    while a % b == 0:
        a //= b
    while b % a == 0:
        b //= a
    return a
```
The above function calculates the greatest common divisor of two numbers a and b, as you specified. It takes the process of finding the smallest common divisor until the numbers are no longer divisible.