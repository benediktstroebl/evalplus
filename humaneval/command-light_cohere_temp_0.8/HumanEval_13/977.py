```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Remove common factors
    while a % b == 0:
        a //= b

    while b % a == 0:
        b //= a

    return min(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The function first checks if either input is zero and returns the non-zero value if true. If both inputs are equal zero, it returns the other input. If one input is not zero and the other is not, it checks if the non-zero input is a factor of the other. Then, it enters a loop to continuously divide the larger input by the smaller input, until the factor is no longer. The code then returns the maximum of the two numbers, which is the greatest common divisor.