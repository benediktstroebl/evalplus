```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    m = max(abs(a), abs(b))
    return max((m, b) // gcd(m, b)), 0

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```