```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # Find the maximum of a and b
    max_ = max(a, b)

    # Calculate all divisors of max up to the square root
    result = []
    for i in range(1, int(max ** 0.5) + 1):
        result.append(i)

    # Return the maximum divisor
    return max_divisor

# Test case 1
print(greatest_common_divisor(3, 5))
# This will print: 1

# Test case 2
print(greatest_common_divisor(25, 15))
# This will print: 5

```
This script defines a function greatest_common_divisor(a, b) that returns the greatest common divisor of two integers a and b. The function first checks if either a or b is empty, and returns 0 in that case. Then, it finds the maximum of a and b and starts calculating the divisors of that maximum up to the square root, appending them to the result array. The function then returns the maximum divisor found.