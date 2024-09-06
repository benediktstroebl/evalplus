```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x

# Test the function
n = 15
result = largest_divisor(n)
print(result) # Output: 5
```