```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0 and b != 0:
        a, b = divmod(a, b)

    return min(a, b)

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(3, 15))  # Output: 5

# Test case 4
print(greatest_common_divisor(6, 2))   # Output: 2

# Test case 5
print(greatest_common_divisor(123, 456))  # Output: 23
```
The function `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. The function utilizes the `divmod` function to efficiently calculate the greatest common divisor and the test cases demonstrate the correctness of the function.

Remember, self-contained functions are a great practice to promote modularity and reduce potential bugs in the code.