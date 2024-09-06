```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        if a % b == 0: 
            a_divisor = b 
        b = b // a 
    return a_divisor 

# Example usage:
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
``` 
This code defines a function `greatest_common_divisor` which computes the greatest common divisor of two integers a and b.  The method involves iterating through the divisors of b until we find a divisor of a which divides a. dry, at which happens to set the divisor to b and continue dividing until b becomes a positive integer which is not divisible by a.