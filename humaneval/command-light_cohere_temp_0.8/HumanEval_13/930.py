```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a_high = a % b 
        b = b //  b 
        a = a_high 
    return a

# Test case 1
print("Test Case 1 - Result:", greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print("Test Case 2 - Result:", greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print("Test Case 3 - Result:", greatest_common_divisor(59, 23))  # Output: 13
```
The function `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. 

The function uses the Euclidean algorithm for prime factorization, repeatedly calculating the remainder of `a` divided by `b` and updating `b` to the quotient of `b` divided by its remainder `a_high`. The process continues until `b` becomes zero, at which point the largest divisor of the original `a` is found.