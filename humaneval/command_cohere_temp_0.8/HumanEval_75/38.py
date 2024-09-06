```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a ** (0.5)) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```

The function `is_multiply_prime` checks if the given number is less than 100 and iterates from 2 up to the square root of that number to check for prime factors.  If the number is divisible by a prime factor, it is removed from the number and added to a list. The function returns `True` if the list of prime factors has exactly three elements, and `False` otherwise. It is efficient because the square root trick allows us to avoid checking prime factors that are obviously too big to be part of a multiplication of three prime factors.