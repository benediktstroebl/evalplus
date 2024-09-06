```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = max(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i

    return m

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(3, 15)))  # Output: 5
print(greatest_common_divisor(10, 15)))  # Output: 5
print(greatest_common_divisor(27, 24)))  # Output: 3
```
This script defines a function called `greatest_common_divisor` that calculates and returns the greatest common divisor of two given integers a and b. The function uses a algorithm to find the greatest common divisor by iterating through possible divisors of the maximum of the two numbers and checking for divisibility. The test cases below demonstrate the example usage of the function with different inputs and expect the correct outputs.