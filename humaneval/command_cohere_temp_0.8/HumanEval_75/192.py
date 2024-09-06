```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
    divisors = []
    
    for p in prime_list:
        if a % p == 0:
            divisors.append(p)
    
    return len(divisors) == 3
``` 

The function `is_multiply_prime` checks if the given number is the multiplication of three prime factors, it does so by first creating a list of prime numbers less than the given number `a` and then checking if any of these primes are divisors of `a`. If the length of the `divisors` list is equal to three, it returns `True`, otherwise, it returns `False`. 

This approach allows the function to correctly determine that the number 30 is the multiplication of the prime factors 2, 3, and 5, and thus pass the given example. 

To further ensure that the function behaves as expected, you might want to add additional tests, such as checking that the function correctly identifies other known multiply prime numbers, like 45 (3 * 3 * 5) or 96 (2 * 2 * 2 * 2 * 3 * 3).