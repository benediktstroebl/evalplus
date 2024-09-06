```python
def greatest_common_divisor(a, b): 
    if not or a == 0 or b == 0:
        return 0  # to avoid division by zero
    return max((d for d in range(1, max(ab)) if (d * a) % b == 0), 1)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 48))  # Output: 12
print(greatest_common_divisor(9, 432))  # Output: 24
```  This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two given integers `a` and `b`. It uses a list comprehension and a built-in function `max()` to iterate through potential divisors and checks if the product of the divisor and the input number `a` is divisible by `b` using the modulo operator. The function returns 1 if the common divisor is found and 0 if none exist.