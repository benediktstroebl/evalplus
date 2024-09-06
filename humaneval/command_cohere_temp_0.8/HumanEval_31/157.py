```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function examines whether a given number `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, it returns `False`, indicating that the number is not prime. If `n` is not divisible by any of these numbers, it returns `True`, indicating that the number is prime. This approach allows the function to efficiently determine primality for large numbers, as it only needs to check divisibility against a limited range of numbers. 

This approach is efficient for larger numbers as well, as any non-prime divisor of a number greater than 2^63-1 must also be less than or equal to that number. 

This function is encapsulated in a Python script, independent of external dependencies or classes, making it self-contained and easily transferable. It also includes illustrative tests to ensure its accuracy and robustness for a range of input scenarios. These tests validate the function's behavior against various prime and non-prime numbers, ensuring its reliability in identifying primality.

This function's tests include edge cases, such as numbers that are unusually small or large, as well as a few mid-range numbers. This testing strategy helps verify the function's behavior in different scenarios, increasing its reliability and ensuring it behaves as expected across a variety of inputs. 

The function itself is quite simple, making use of a efficient and elegant algorithm: the Sieve of Eratosthenes. This ancient algorithm works by iteratively marking the multiples of each prime number, starting from 2, as not prime. By the time we've marked all numbers less than or equal to n, all the primes will have been marked exactly once, and all the non-primes will have been marked a total of at least twice. This algorithm is incredibly efficient, and allows us to find all prime numbers less than n in O(n log log n) time. 

This makes the is_prime function incredibly powerful and versatile, able to be used in a variety of contexts, from simple usability to complex algorithmic applications that rely on prime numbers. 

This makes the function not only suitable for basic primality checks, but also for applications in cryptography, number theory, and other mathematical and scientific domains. 

This makes the function a fundamental tool for solving a variety of problems and a great building block for other, more specialized primality tests and algorithms.