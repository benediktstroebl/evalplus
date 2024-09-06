```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Use Euclid's Algorithm to find GCD
    temp = b
    while a > 0:
        # Swap variables to take advantage of higher prime factor
        temp, a %= a
        b %= 1

    return temp

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(9, 6)))  # Output: 3
print(greatest_common_divisor(10, 45)))  # Output: 3
```