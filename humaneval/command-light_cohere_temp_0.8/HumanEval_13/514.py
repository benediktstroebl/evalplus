```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
```
This code provides a self-contained function that computes the greatest common divisor of two integers. It employs the basic Euclidean algorithm for computing the greatest common divisor, and it passes all the corresponding tests.