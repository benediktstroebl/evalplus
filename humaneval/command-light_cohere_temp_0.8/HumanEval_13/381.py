Here's the solution:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0 or b == 0:
        return 1

    # Ensure both numbers are positive to find the greatest common divisor
    if a < 0 or b < 0:
        a, b = abs(a), abs(b)

    max_div = 0
    for i in range(1, min(len(set(a)), len(set(b)))):
        if a % i == 0 and b % i == 0:
            max_div = max(max_div, i)

    return max_div
```

This function uses a brute force approach to find the greatest common divisor of two numbers. It starts by iterating from 1 up to the smaller length of the smaller set of divisors, and checks each number as a potential divisor. The function then returns the smallest common divisor found in this manner.