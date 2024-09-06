```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # Calculate the gcd using the extended Euclidean algorithm
    gcd = (a, b) while gcd[0] != gcd[1]:
        a, b = gcd[1], gcd[0]
    
    return gcd[0]

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This Python function named `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. It employs the extended Euclidean algorithm to efficiently compute the gcd.  The also checks for special cases: when either input number is 0, it returns the other as the gcd.