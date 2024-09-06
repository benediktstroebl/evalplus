Here is a Python script that contains a self-contained function that calculates the greatest common divisor for two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
gcd_test = greatest_common_divisor(3, 5)
print("GCD of 3 and 5 is:", gcd_test)
gcd_test = greatest_common_divisor(25, 15)
print("GCD of 25 and 15 is:", gcd_test)
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor for two integers `a` and `b`. The function also includes a helper function `gcd` which computes the greatest common divisor using the Euclidean algorithm. The usage example demonstrates how to use the function with test cases.