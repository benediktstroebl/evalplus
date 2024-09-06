```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    a = 25
    b = 15
    print(greatest_common_divisor(a, b))  # Output: 5
```