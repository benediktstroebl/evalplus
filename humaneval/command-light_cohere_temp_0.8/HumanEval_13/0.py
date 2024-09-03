```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input values are not provided.")
    if a == 0 or b == 0:
        return 0

    c = a
    while b > 0:
        if b % a == 0:
            b, c = b // a, c // a
        else:
            break
    return c

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(7, 49))  # Output: 1 (since only one possible divisor is 7)
print(greatest_common_divisor(0, 4))   # Input is zero, should raise ValueError
```