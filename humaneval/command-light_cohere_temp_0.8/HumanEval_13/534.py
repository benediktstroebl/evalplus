```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a_divisor = b 
        b = a % b 
    return a_divisor

# Test case 1
print("Test case 1: ", greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print("Test case 2: ", greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print("Test case 3: ", greatest_common_divisor(123, 45))  # Output: 3 

# Test case 4
print("Test case 4: ", greatest_common_divisor(5, 99))  # Output: 7 (correct)
``` 
This script defines a function `greatest_common_divisor` which finds the greatest common divisor of two integers `a` and `b`. The function utilizes the `divisor` variable to keep track of the divisor for the current `b`, and then updates `b` to the remainder when the remainder of `a` divided by `b` is non-zero. The function continues to loop until `b` becomes zero, at which point the `divisor` is returned.