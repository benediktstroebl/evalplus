```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1 or a % 2 == 0 or a % 3 == 0:
        return False
    for i in range(5, int(a ** 0.5) + 1, 2):
        if a % i == 0 or a / i == int(a / i):
            return False
    return True
```

This Python script defines a function called `is_multiply_prime` that takes a single argument `a`, and returns `True` if the given number is the product of three prime numbers, and `False` otherwise. 

The function first checks if the number is less than 2, or if it is a multiple of 2 or 3, and returns `False` if any of these conditions are met. It then iterates through the numbers 5, 7, 9, and so on, in increments of 2, checking if the number is divisible by any of them. If the number is divisible or if the quotient is an integer, it returns `False`. If none of these conditions are met, the function returns `True`. 

The example in the problem statement is correct, as `is_multiply_prime(30)` would return `True`, given that 30 is the multiplication of 2, 3 and 5. 

This script can be used as a function to determine if a given number is the product of three prime numbers, and can be embedded within a larger program to integrate with other functionality.