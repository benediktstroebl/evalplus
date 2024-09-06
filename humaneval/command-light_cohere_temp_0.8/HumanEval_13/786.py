```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(d for d in range(1, min(a, b)) + 1 if not (a % d or b % d))

# Example function call:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
The function greatest_common_divisor calculates the greatest common divisor of two integers a and b. The function returns the value of the divisor which is less than the minimum of a and b, ensuring that the result is a positive integer.

The example function calls demonstrate how to use the function with specific numbers and verify the returned result.