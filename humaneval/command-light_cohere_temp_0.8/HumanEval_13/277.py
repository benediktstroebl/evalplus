```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # if both numbers are even, we take their highest power of 2 as GCD
    # so we start with the max power of 2 less than the smaller number
    # this ensures we find the correct result faster
    power_a = 1
    while a > 0:
        if a % 2 == 0:
            power_a += 1
        a //= 2

    # similarly we find the power of 2 for b
    power_b = 1
    while b > 0:
        if b % 2 == 0:
            power_b += 1
        b //= 2

    # at this point we have the powers of a and b with respect to 2
    # so we multiply them and return
    return power_a * power_b

# test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(7, 12))  # Output: 4
print(greatest_common_divisor(13, 11))  # Output: 3
```