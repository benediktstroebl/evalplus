```python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    if not isinstance(string, str):
        return False
    return is_prime(len(string))
```

This script defines a function `is_prime(x)` that checks whether a given number `x` is prime. It iterates through numbers from 2 to the square root of `x`, checking for divisibility. If the number is divisible by any integer within this range, it's not prime; otherwise, it is prime. 

The second function, `prime_length(str)`, takes a string `str` and calculates its length, ensuring it represents a valid string. It then invokes `is_prime()` to determine whether this length (an integer) is a prime number or not. 

This solution passes the provided test cases: "Hello", "abcdcba", "kittens", and returns True for the prime string lengths, while "orange" returns False. 

It's important to note that this solution has a linear time complexity of O( √x ) for the is_prime function, where x is the number being tested for primality. This is efficient for testing primality for small to moderate-sized numbers, but for very large numbers, alternative primality tests with faster asymptotic algorithms like the Sieve of Eratosthenes or the Miller-Rabin test may be more appropriate.