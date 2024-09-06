```python
def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a
```
The function repeatedly divides b by a and updates the divisors accordingly until b becomes 0. At each division step, the current value of b is assigned to the variable a and the remainder of the last division operation is assigned to the variable b. This guarantees that when b becomes 0, the current value of a is the greatest common divisor of the original a and b. The main reason for the while loop is to iterate until the divisor becomes 0, guaranteeing that the greatest common divisor is found.