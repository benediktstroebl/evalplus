```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a%b
    return a

# Example usage
n = 15
print(largest_divisor(n))
```