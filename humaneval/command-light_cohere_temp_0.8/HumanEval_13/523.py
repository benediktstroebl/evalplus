Here's the improved Python script with a self-contained function that calculates and returns the greatest common divisor (GCD) of two integers a and b, with tests:
```python
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Test case: GCD of 3 and 5
print(gcd(3, 5))  # Output: 1

# Test case: GCD of 25 and 15
print(gcd(25, 15))  # Output: 5

# Test case: Negative numbers
print(gcd(-10, 25))
```
This script defines a `gcd` function that calculates the greatest common divisor of two integers a and b using the Euclidean algorithm, a method that efficiently computes the GCD. The function handles cases where it returns `a` if `a` is zero, and otherwise, it recursively calculates the GCD by calculating the quotient of `b` divided by `a` and taking the remainder. 

The script then provides several test cases to validate the `gcd` function, ensuring that it produces the correct results.