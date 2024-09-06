Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking whether the number is divisible by any integer in this range. If the number is divisible by any of these integers, it returns `False`. If it is not, it returns `True`.

This algorithm is a straightforward approach to testing primality and is efficient for larger numbers due to its use of the square root technique. However, it is worth noting that this method is not suitable for very large numbers, as the computation of the square root can result in significant computational overhead. More sophisticated algorithms, such as the Sieve of Eratosthenes or the Miller-Rabin test, are preferred for checking the primality of large numbers. Nonetheless, the provided function offers a simple and effective approach for testing primality in many practical scenarios.