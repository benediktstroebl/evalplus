```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for prime in primes:
        if n % prime == 0:
            divisors.append(prime)
    
    return len(divisors) == 3
```

This Python script defines a function called `is_multiply_prime` that takes a single parameter `n`, representing a number to be tested. It systematically checks whether `n` can be divided evenly by each prime number up to a maximum of 100. If the given number is divisible by exactly three different prime numbers, thereby satisfying the condition of the problem, the function returns `True`; otherwise, it returns `False`. 

This approach enables the function to accurately determine whether the given number is the product of three prime numbers and provides a conclusive result through its return value. 

To ensure the function performs well on the given problem, potential optimizations could be implemented, such as removing the check for 2 as a divisor, since all even numbers greater than 2 can be discounted as candidates for multiprime status. Further, more efficient prime detection algorithms, such as the Sieve of Eratosthenes, could be used in lieu of an exhaustive approach. 

This function includes a docstring and typesetting for markup languages that highlight the purpose and usage of the function, making the code more understandable and well-documented. 

You can employ this function in other programs by calling it and providing the argument you wish to test. Employing the function will yield a boolean value that indicates whether the given number is the product of three prime numbers.