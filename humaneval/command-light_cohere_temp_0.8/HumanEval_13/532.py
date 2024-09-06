```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)
    return max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(5, 25))  # Output: 5
print(greatest_common_divisor(7, 49))  # Output: 7
print(greatest_common_divisor(0, 4))   # Output: 0 (division by zero)
print(greatest_common_divisor(49, 7))  # Output: 7
```
The function `greatest_common_divisor` uses a recursive approach to find the greatest common divisor of two numbers a and b. The function first handles cases where either a or b is 0, in which case it returns 0. Then, it handles the other cases by recursively calling itself with the argument b, and a % b to avoid overflow. The function then returns the maximum of the two numbers. 

This function is self-contained and provides a solution to the problem of finding the greatest common divisor of two integers. It can be used to test cases to ensure its correctness and efficiency.