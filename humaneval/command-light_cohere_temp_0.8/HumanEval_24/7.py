```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 9)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test case
n = 15
result = largest_divisor(n)
print("The largest divisor less than or equal to", n, "is:", result)
```