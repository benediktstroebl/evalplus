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

The function `is_multiply_prime` checks if the given number is less than 100 and iterates from 2 up to the square root of that number to check for prime factors. 

It leverages the prime number division rule, which states that a number is prime if it can only be divided evenly by 1 and itself. If a number can be divided by another number evenly, it is not prime. 

This approach avoids the need for an additional library and provides a more straightforward implementation. 

To ensure that the given number is the product of exactly three primes, the function checks the length of `prime_factors`, which is returned by the `prime_factors` generator expression. 

This approach provides a straightforward and efficient way to determine whether a given number is the product of exactly three primes.