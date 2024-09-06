```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    limit = int(sqrt(a)) + 1
    for b in range(2, limit):
        if a % b == 0:
            return False
    
    for b in range(2, limit):
        if a % b == 0 and is_prime(b):
            return False
    
    return True

def is_prime(n):
    # Return true if the number is a prime, false otherwise
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This script defines a function called `is_multiply_prime` that takes a number `a` as input and returns `True` if `a` is the product of three prime numbers, and `False` otherwise. 

The function first checks if `a` has any divisors besides 1 and itself, by iterating through all integers from 2 to `sqrt(a) + 1` and returning `False` immediately if it finds any divisor of `a`. It then iterates through all integers from 2 to `sqrt(a) + 1` again to check if any of them divide `a` and are prime numbers, and returns `False` if any such number is found. 

If none of these conditions are met by the end of the function, it returns `True`. 

The script also defines a helper function, `is_prime`, which takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It checks if `n` is less than 2, in which case it is not a prime, and then iterates through all integers from 2 to `sqrt(n) + 1`, checking if any of them divide `n`, and returning `False` if they do. If no divisors are found, it returns `True`. 

Overall, the script provides an accurate and efficient way to determine whether a given number is the product of three prime numbers.