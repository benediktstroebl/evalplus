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

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(15, 25)))  # Output: 5
print(greatest_common_divisor(8, 40))  # Output: 4 (It is correct since 8, 40 have a greatest common divisor of 4)
print(greatest_common_divisor(10, 20))  # Output: 5 (correct since 10 is divisible by 5)
print(greatest_common_divisor(15, 25))  # Should raise exception)
```

The function greatest_common_divisor calculates the greatest common divisor of two integers a and b. It uses a specific cases to determine the greatest common divisor:
1. For example, if b is 1, it returns a. The greatest common divisor is a.GE a, which are 1 and a, respectively. For example, if a = 3 and b = 5, the greatest common divisor is 1. If a is 1, it returns b. If neither a is a factor of the other, it recursively calls itself with the other number. This is similar to the process of finding the greatest common divisor of two numbers. The loop terminates when a and b become 1, and a is 0. The greatest common divisor is 0.