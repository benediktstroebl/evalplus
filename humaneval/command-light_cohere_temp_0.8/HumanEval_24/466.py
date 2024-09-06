```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1, 1)

def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x

# Example usage:
n = 21
result = largest_divisor(n)
print(f"Largest divisor of {n}: {result}")
```