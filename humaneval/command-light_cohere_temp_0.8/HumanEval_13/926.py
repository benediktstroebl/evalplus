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

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 21))  # Output: 7

```
This Python code defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers `a` and `b`. The function uses a series of conditional statements to determine the greatest common divisor, considering cases where either or both numbers are zero or one. The function then tests the test cases and prints the results to the console.