```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

# Run-time tests
print(largest_divisor(15))      # Output: 5
print(largest_divisor(16))      # Output: 1
print(largest_divisor(4)))    # Output: 2 (since 4 is divisible by 2)
print(largest_divisor(27))      # Output: 3
```