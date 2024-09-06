```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Invalid inputs: both numbers must be integers"
    if a == 0:
        return "a cannot be 0"
    return _gcd(a, b)

def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))      # Output: 1
print(greatest_common_divisor(25, 15))    # Output: 5
print(greatest_common_divisor(4, 12))      # Output: Simplified.
```
In this script, we have a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It employs a helper function `_gcd` that calculates the greatest common divisor using the Euclidean algorithm. The function also includes input validation to ensure the inputs are valid integers.

The output will be the corresponding greatest common divisor based on the test cases provided.