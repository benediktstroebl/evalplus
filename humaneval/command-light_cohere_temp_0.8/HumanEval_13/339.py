```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(f"Result of gcd({input(), input()}) = {gcd(input(), input())}")
```
The function `greatest_common_divisor` calculates the greatest common divisor of two integers `a` and `b`. The function efficiently computes the greatest common divisor by utilizing the `gcd` helper function, which implements the Euclidean algorithm for finding the greatest common divisor.  The use this if you want to test your function with different inputs!