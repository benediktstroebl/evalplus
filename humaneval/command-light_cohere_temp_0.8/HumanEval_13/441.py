```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(a, b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
This code provides a function `greatest_common_divisor` that computes the greatest common divisor of two numbers. It also includes a testing various inputs and ensuring the function's correctness.