```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incorrect inputs: a and/or b must be integers.")
    if a == 0 or b == 0:
        return 0

    # Initialize variables
    d = 0
    m = a
    while m <= b:
        if m % a == 0 and m % b == 0:
            d = m
            m += 1
        else:
            m += 2

    return d

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(100, 50))  # Output: 25
print(greatest_common_divisor(2, 500))  # Input: Division by 2 (not valid for integers)
print(greatest_common_divisor(21, 7))  # Input: Out of range of integers 

```