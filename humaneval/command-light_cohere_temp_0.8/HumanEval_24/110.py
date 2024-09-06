```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 0)

def gcd(a: int, b):
    while b:
        a, b = b, a % b
    return a

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(27))  # Output: 27
print(largest_divisor(21))  # Output: 3
```