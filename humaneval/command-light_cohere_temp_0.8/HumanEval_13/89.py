```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: Input arguments are not valid"
    if a == 0 or b == 0:
        return "Error: Both numbers are zero"
    
    # Calculate gcd using recursive approach
    def gcd_helper(x, y):
        if y == 0:
            return x
        return gcd_helper(y, x % y)
    
    return gcd_helper(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 6))   # Output: 2
print(greatest_common_divisor(10, 55))  # Output: 5
```
The code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The function first handles corner cases like invalid inputs and zero divisors. Then, it employs a recursive approach to determine the greatest common divisor. Finally, it executes four test cases that validate the function's behavior.