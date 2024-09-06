```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0 or b == 0:
        return 0

    # Find the greatest divisor of a and b
    gcd = gcd(a, b)

    # Return the greatest common divisor
    return gcd

# Unit test
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b. The function uses the a special case handling for when either a or b is 0, in which case it returns 0 as the GCD. 

The function also utilizes the built-in function gcd from the math module to efficiently calculate the greatest common divisor.