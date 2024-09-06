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
    print(f'Greatest Common Divisor: {gcd(15, 25)})
    print(f' testing with {(15, 25), (5, 6)})')
``` 
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function utilizes the `gcd` function to compute the greatest common divisor recursively. The `gcd` function implements the specific Euclidean algorithm to find the greatest common divisor of `a` and `b`. The code also includes a `main` block with test cases to demonstrate the functionality.