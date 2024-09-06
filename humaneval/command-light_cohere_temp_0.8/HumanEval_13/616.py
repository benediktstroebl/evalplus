```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test case for function
if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor between {a} and {b} is {gcd(a, b)} = {gcd(a, b)} = 5")
```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers using the `gcd` function. It then defines theaya helper function `gcd` which calculates the greatest common divisor using the Euclidean algorithm. The main function tests the tested case of a and b, and the output is printed to the console.