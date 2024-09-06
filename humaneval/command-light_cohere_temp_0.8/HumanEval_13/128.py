```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return abs(a - b)

if __name__ == "__main__":
    a = 3
    b = 5
    print(f"GCD of {a} and {b} is {greatest_common_divisor(a, b)} = {b}")
```