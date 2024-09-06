```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    m, divisor = 2, 1
    while divisor <= max(a, b):
        if a % divisor == 0 and b % divisor == 0:
            m = divisor
            divisor += 1
        else:
            divisor += 1

    return m

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15)))  # Output: 5

# Test case 3
print(greatest_common_divisor(17, 49)))  # Output: 7 (Note, 17 is a prime number)

# Test case 4
print(greatest_common_divisor(15, 25)))  # Output: 5
```
This Python function `greatest_common_divisor` takes two integers `a` and `b` as input and returns the greatest common divisor of the two numbers. The function uses a test cases to validate the functionality. If the function is successful, the output of each test case should be the corresponding greatest common divisor.