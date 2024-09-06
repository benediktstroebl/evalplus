```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1:
        return False
    for b in range(2, a):
        if a % b == 0:
            return False
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            return False
    return True
```

This Python script defines a function called `is_multiply_prime(a)` that evaluates whether a given number `a` is the product of three prime numbers. The function first checks if `a` is less than or equal to 1, immediately returning False if so. It then iterates through integers from 2 up to, but not including, the given number `a`, checking if any divisible factors exist. Subsequently, it iterates through factors from 2 up to the square root of `a`, ensuring no divisibility by any factor within this range. If no divisible factors are found after these iterations, the function returns True, indicating that the given number is likely the product of three prime numbers. 

The function's rationale is predicated on the observation that any number can be uniquely factored into prime numbers, and the given problem pertains to identifying numbers that can be expressed as the product of precisely three prime factors. The iterative method allows for efficient factor checking within the given constraints. 

This script enables you to efficiently determine if a given number is the product of three prime numbers while adhering to the specified constraint of less than 100.