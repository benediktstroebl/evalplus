```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")

    if not a % b == 0:
        return 0

    return (b + 1) // gcd(a, b + 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15

    print("GCD:", end=":", a, b, gcd(a, b))
    print("GCD:", end=":", a, b, "=", a % b)
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers a and b. Using the Euclidean algorithm to find the greatest common divisor efficiently.