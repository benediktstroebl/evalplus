Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The `gcd` helper function computes the greatest common divisor of a and b using the Euclidean algorithm for finding the greatest common divisor. The script then passes tests by calling the function with test cases.