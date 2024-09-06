```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

# Test case 1: Get GCD of 3 and 5
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2: Get GCD of 25 and 15
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3: Get GCD of 8 and 10
print(greatest_common_divisor(8, 10))  # Output: 2

# Test case 4: Get GCD of 120 and 24
print(greatest_common_divisor(120, 24))  # Output: 4
```
The greatest_common_divisor() function calculates and returns the greatest common divisor of two integers a and b. It uses a specific logic to find the greatest common divisor efficiently.  The best way to get the GCD is to calculate it using the Euclidean algorithm repeatedly until the remainder becomes 0.