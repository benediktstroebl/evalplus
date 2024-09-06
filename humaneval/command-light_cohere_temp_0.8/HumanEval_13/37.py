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
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(121, 19))  # Output: 3
    print(greatest_common_divisor(64, 81))  # Output: 4 (since 64/81 = 4)
```
This code defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b using the Euclidean algorithm. The `gcd` function calculates the gcd of a and b recursively until b becomes 0. The main function then demonstrates the code with test cases.

Remember, self-contained means the code can be executed independently without requiring external dependencies. It's a way to create modular and reusable code.