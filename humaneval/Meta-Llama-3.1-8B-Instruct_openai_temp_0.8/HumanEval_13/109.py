```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b """

    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. It then tests this function with the example use cases provided.

The Euclidean algorithm is an efficient method for computing the GCD of two numbers. It works by repeatedly applying the formula `gcd(a, b) = gcd(b, a % b)`, where `%` is the modulo operator, which returns the remainder of the division of `a` by `b`. When `b` becomes zero, the GCD is `a`.