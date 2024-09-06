```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0  # To handle potential division by zero

    # Loop through divisors up to the square root of min(a, b)
    for i in range(1, int(math.sqrt(min(a, b)) + 1)):
        if a % i == 0 and b % i == 0:
            return i

    # If no common divisor is found, return None
    return None

# Example usage:
# Test function with a and b values passed as arguments
def test_greatest_common_divisor(a, b):
    return greatest_common_divisor(a, b) == 1

# Test case 1:
test_greatest_common_divisor(3, 5)  # Output: True

# Test case 2:
test_greatest_common_divisor(25, 15)  # Output: True

# Test case 3:
test_greatest_common_divisor(13, 49)  # Output: True

# Test case 4:
test_greatest_common_divisor(7, 21)  # Output: True
```
The test cases aim to verify if the function correctly calculates the greatest common divisor. You can add more test cases to further evaluate the function's behavior.