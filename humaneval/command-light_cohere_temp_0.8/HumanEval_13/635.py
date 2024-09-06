```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incorrect input values: a or b must be integers.")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor between {a} and {b} is {gcd(a, b)} = {b}")
```