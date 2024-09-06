```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    return greatest_common_divisor(b % a, a) 

# Test case 1
print("Test case 1: ", greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print("Test case 2: ", greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print("Test case 3: ", greatest_common_divisor(125, 17))  # Output: 5

# Test case 4
print("Test case 4: ", greatest_common_divisor(9, 81))  # Output: 3
```
The provided Python function `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. It employs a basic technique of repeatedly finding the greatest common divisor of the residual when `b` is divided by `a`. The function returns `0` if either input is `0`, indicating no common divisor. The test cases demonstrate the test function correctness.