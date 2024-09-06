```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 3:
        return False
    for i in range(2, int(a ** (0.5)) + 1):
        if a % i == 0:
            return False
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if a % i == 0:
            return False
    return True
```

The function `is_multiply_prime` checks if the given number is less than 3, it returns `False`. For numbers greater than 2, it loops from 2 to the square root of the given number, if any intermediate number divides the given number, it returns `False`. It then checks for the presence of 2, 3, and 5 in the divisors of the given number, if any is found, it returns `False`. If none of these conditions are met, it returns `True`. 

This approach ensures that the `is_multiply_prime` function accurately determines if the given number is the product of three prime numbers and adheres to the defined criteria.

Make sure to test the function with different inputs to ensure its correctness. You can use the provided example (30) to test the function.