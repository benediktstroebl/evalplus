```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function returns `True` if the given number is prime, and `False` otherwise. It first checks if the given number is less than 2, and since primes are defined to be greater than 1, it returns `False` in such a case. It then starts a loop from 2 and goes up to the given number, checking whether the number is divisible by any other number. If the number is divisible by any other number, it returns `False`. However, if the loop completes without finding a divisor, it returns `True`.

This algorithm is relatively efficient because it eliminates multiples of numbers one by one, reducing the possible options for the original number at each step. It's a fundamental part of prime detection, used in more complex algorithms like the Sieve of Eratosthenes. 

This approach has been used since it was discussed in the ancient world, especially by the ancient Greeks, and is a key algorithm in number theory.