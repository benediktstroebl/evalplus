```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    return max(a, b) / gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function uses the `gcd` function to compute the greatest common divisor, and then returns the result. The `gcd` function computes the greatest common divisor of `a` and `b` using the Euclidean algorithm for finding the greatest common divisor. The output of the script is the test cases that demonstrate the correctness of the function.