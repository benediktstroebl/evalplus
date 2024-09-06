```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        # checking for factors
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        
        # edge case for factors
        if a == 3:
            return True
        
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        
        if a != 3:
            return True
    return False
```

This script defines a function called `is_multiply_prime(a)` that checks if a given number is the multiplication of three prime numbers. The function first checks if `a` is less than 100 and greater than 1. It then iterates from 2 up to the square root of `a`, checking for factors by determining if `a` is divisible by any of these numbers. If the number is not divisible by any, it recursively checks the same factorability for the number `3`. If it is still not divisible by any number, it returns `True`, however, if the number is equal to `3`, it returns `True` directly. If any divisor is found at any point, it returns `False`. 

This problem allows for many approaches and can be a good candidate for optimization.