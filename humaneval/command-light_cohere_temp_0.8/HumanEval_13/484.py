```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given")
    if a == 0 or b == 0:
        return 0
    gcd = []
    while a != 0 and b != 0:
        gcd.append(ord(a % b))
        a, b = b, a - (a % b)
    return gcd[0]

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(6, 18) == 6
assert greatest_common_divisor(9, 81) == 9
assert greatest_common_divisor(27, 54) == 27
```