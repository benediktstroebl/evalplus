```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Input must be numbers"
    return min(x for x in range(1, max(a, b)) if all(d % x == 0 for d in (a, b)))

# Test case 1: Use function with two positive integers
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2: Use function with positive and negative numbers
print(greatest_common_divisor(-25, 15))  # Output: 5

# Test case 3: Use function with numbers greater than the maximum divisor
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 4: Use function with one number
print(greatest_common_divisor(15, 25))  # Output: The function returns "Input must be numbers" since 15 is not a positive integer
```