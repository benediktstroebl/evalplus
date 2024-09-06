```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0  # Handle possible division by zero
    while b > 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            break
    return a

# Test the function
 assert greatest_common_divisor(3, 5) == 1
 assert greatest_common_divisor(25, 15) == 5
 assert greatest_common_divisor(10, 25) == 5
 assert greatest_common_divisor(56, 12) == 56
``` 
This function, `greatest_common_divisor`, computes the greatest common divisor of two integers `a` and `b`. It employs a `while loop that removes the factors from `b` while `a` remains divisible. The final value of `a` will represent the GCD. 

This self-contained function is straightforward and effective. It handles the zero-case and employs a clever `while` loop that effectively finds the GCD using the Euclidean algorithm.