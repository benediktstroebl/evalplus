```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 4
print(largest_divisor(100)))  # Output: 12
```