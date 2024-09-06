```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
``` 

This function revolves around the primality test, which is one of the fundamental techniques for determining whether a number is prime. It iterates through numbers from 2 up to the target number and checks if the target can be divided evenly by any of them. If it can, then the number is not prime, and the function returns `False`. If no divisors are found, the function returns `True`, indicating that the number is prime. 

This approach is elementary and efficient, making it suitable for the majority of use cases related to primality testing. 

For larger numbers, advanced techniques like the Sieve of Eratosthenes or the Miller-Rabin test may be more efficient. However, the provided function offers a straightforward solution that maintains simplicity and clarity while effectively handling the majority of primality assessment tasks.