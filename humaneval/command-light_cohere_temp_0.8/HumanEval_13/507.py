```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor is: {gcd(a, b)}")
```
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers `a` and `b`. It also includes a helper function `gcd` that uses the Euclidean algorithm to compute the greatest common divisor of two numbers using the `pop` function. 
The `__main__` block contains sample inputs and calls the `greatest_common_divisor` function with those inputs, and prints the result.