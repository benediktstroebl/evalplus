```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    dirs = max(a, b)
    while d % a != 0 or d % b != 0:
        d += 1
    return d

# Example function call to test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either number is zero, and if so, returns 0 as the GCD. Then, it uses the maximum of the two numbers as the initial candidate for the GCD. After that, it enters a loop that keeps incrementing the divisor d until it becomes the common divisor of a and b. The value of d at the first occurrence of the loop is returned as the GCD.