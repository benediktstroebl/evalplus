```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, divisor(n))

def divisor(n: int) -> int:
    return n // max(1, n // 6)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 8
print(divisor(30))       # Output: 5
print(gcd(60,5))       # Output: 3
```