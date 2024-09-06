Here's the self-contained Python script with the function `greatest_common_divisor` that solves the problem and passes the tests:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Returns the greatest common divisor of two integers a and b."""
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b%a, a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 4))  # Output: 4
print(greatest_common_divisor(105, 3))  # Output: 3
```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers. It utilizes the method of finding the greatest common divisor: If the denominator becomes zero, the GCD is the numerator, and vice versa. The function handles the recursive calculation, ensuring that the result is correct for any pair of input values.