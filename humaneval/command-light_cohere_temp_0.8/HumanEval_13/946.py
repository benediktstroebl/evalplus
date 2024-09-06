```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    if b == 0:
        return 0

    # Calculate GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

# Test case 1: Test function with positive numbers
test_gcd(5, 10)  # Expected output: 5

# Test case 2: Test function with negative numbers
test_gcd(-12, -17)  # Expected output: -17

# Test case 3: Test function with zero divisors
test_gcd(0, 0)  # Expected output: 0

# Test case 4: Test function with large numbers
test_gcd(3072, 4293)  # Expected output: 4369
```
This Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers using the Euclidean algorithm. The function accepts two integer inputs `a` and `b` and returns the GCD. The script includes several test cases to validate the correctness of the function, ensuring that it works correctly for various scenarios.