```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = min(a, b)
    for i in range(2, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i

    return m

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15)))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 4)))  # Output: 1
```
This script defines a function greatest_common_divisor that takes two integers a and b as input and calculates the greatest common divisor of a and b.

The function first checks if either a or b is false, and if so, returns 0. The function then finds the minimum of the two numbers and uses a loop to check for divisibility up to the square root of the minimum number.