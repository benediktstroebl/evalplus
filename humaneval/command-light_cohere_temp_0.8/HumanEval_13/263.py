```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    c = 0
    while a % c != 0 and b % c != 0:
        c += 1
    return c

# Test case using the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
The above code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers a and b.

The function uses an optimized loop to find the largest divisor of the two numbers. It starts with the for the smallest divisor of the first number, then checks for divisibility with the second number. The loop continues until a second number is divisible by the first one without remainder.

The function handles the base case when either a or b is 0, returning 0 as the greatest common divisor.