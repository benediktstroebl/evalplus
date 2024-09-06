Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Test cases
print(gcd(3, 5))  # Output: 1
print(gcd(25, 15))  # Output: 5
```

This code defines a function gcd that calculates the greatest common divisor of two integers a and b using the Euclidean algorithm. The function returns the specific, and the test cases pass without errors, indicating that the function is correct and self-contained.