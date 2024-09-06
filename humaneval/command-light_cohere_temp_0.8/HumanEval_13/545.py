```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Cannot find a non-zero divisor.")
    return max(a, b) // gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor of {a} and {b} is {gcd(a, b)} = {b}")
```