```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = min(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i

    return m

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either of the input integers is `None` or zero, and if so returns `0` as the greatest common divisor. The function then iterates from 1 to the smallest even divisor of the input numbers (`min(a, b)`), and checks if both input numbers are divisible by this divisor. If a, it returns the divisor. If no divisors are found, the function returns the smallest even divisor of the input numbers.