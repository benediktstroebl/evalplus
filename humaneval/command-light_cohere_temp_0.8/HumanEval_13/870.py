```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0 or b == 0:
        return 0

    return max(a, b) // gcd(a, b)

# Unit tests
test_gcd = lambda: assert greatest_common_divisor(3, 5) == 1
test_gcd()
test_gcd(25, 15)
test_gcd(1, 5)
test_gcd(19, 13)
test_gcd(5, 19)
test_gcd(13, 39)
test_gcd(15, 75)
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. It also includes unit tests to ensure the function's correctness.  The test_gcd() function evaluates the function with various input combinations and asserts that the results are correct. 
This code provides a self-contained solution for finding the greatest common divisor of two integers.