```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Invalid inputs.
    while a smallest_common_divisor(a % b):
        a //= a % b
    while not b:
        a += 1
        b = a % b
    return a
``` 
This function takes two integers a and b as input, it then calculates the greatest common divisor of a and b by iteratively finding the GCD of a and b until b is 0 or 1. The function then returns the minimum of a or b, which is the GCD of a and b.