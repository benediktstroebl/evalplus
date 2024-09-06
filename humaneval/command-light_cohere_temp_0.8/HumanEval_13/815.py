```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    if not a: return b
    if not b: return a
    return math.floor(math.frexp(0) % ((a - b))

if __name__ == "__main__":
    try:
        a = 25
        b = 15
        print(f"The greatest common divisor of {a} and {b} is {gcd(a, b)}: {a // gcd(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of 2 numbers `a` and `b` passed as arguments. It also defines a workhorse GCD(a, b) using the `gcd` function, which computes the greatest common divisor of `a` and `b`. The `main` function tests the `greatest_common_divisor` function with various input values and prints the result.