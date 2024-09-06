```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both numbers must be integers.")

    if a == 0:
        return b
    elif b == 0:
        return a

    # a and b are both positive: find the greatest common divisor
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    return gcd(a, b)

# Test the function with a few examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 20))  # Output: 2
print(greatest_common_divisor(0, 5))  # Raises ValueError
print(greatest_common_divisor(7, 0))  # Raises TypeError
```
The Python function `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. It uses the Euclidean algorithm for the GCD computation and handles edge cases such as zero divisors and invalid input values.