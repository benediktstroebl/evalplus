```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    if a == b:
        return a
    if b == 1:
        return a
    t = greatest_common_divisor(b, mod_pow(a, b - 2))
    if t == 1:
        return t
    return greatest_common_divisor(a, t)

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 48))  # Output: 2 (divisible by 2 and 1 times 48)
print(greatest_common_divisor(36, 12))  # Input, with possible overflow during calculation)
print(greatest_common_divisor(121, 7))  # Input, with possible overflow during calculation)
```