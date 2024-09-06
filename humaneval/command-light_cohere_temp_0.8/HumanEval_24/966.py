```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    n = 15
    print(f"The largest divisor of {n} is {largest_divisor(n)}:")
```