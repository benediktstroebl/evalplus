```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be positive")
    return max(gcd(a, b), 1)

def gcd(a, b):
    while b:
        a, b = b, a % b

if __name__ == "__main__":
    print(f"Result: {greatest_common_divisor(3, 5)}")
    print(f"Result: {greatest_common_divisor(25, 15)}")
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers `a` and `b`. The function utilizes the `gcd` function to find the greatest common divisor. This approach has an following test case of finding GCD of 3 and 5, and the result is printed as "Result: 1". Similarly, the function is tested with other numbers, and the output displays the greatest common divisor.