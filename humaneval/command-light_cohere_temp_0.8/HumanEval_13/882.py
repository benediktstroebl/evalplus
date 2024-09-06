```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incompatible inputs: a and b must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
a = 25
b = 15
print(greatest_common_divisor(a, b))  # Output: 5
```
This function computes the greatest common divisor of two numbers a and b, ensuring proper input validation and utilizing the efficient gcd function for prime factor decomposition.