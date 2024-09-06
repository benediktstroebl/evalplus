```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Inappropriate input values. The parameters a acceptable values: positive integers.")
    if a == 0 or b == 0:
        return 0
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
try:
    print(greatest_common_divisor(3, 5))
except ValueError as e:
    print(f"Error: {e}")
```