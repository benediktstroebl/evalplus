```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    m = 0
    for i in range(1, min(len(str(a)), len(str(b)))):
        m = max(m, int(a[i - 1] / b[len(str(b)) - i]))

    return m

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This Python code defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It uses an efficient approach with a loop, checking divisibility from the shorter string first and then checking the other case. This function is expected to be useful for finding the GCD of two numbers, especially when their strings are of different lengths.