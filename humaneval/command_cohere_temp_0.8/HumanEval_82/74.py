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

This script defines a function `is_prime(num)` that checks whether a given number is prime or not. It employs a simple optimization by checking only up to the square root of the number, iterating from 2 to the square root of the number, and returning False immediately if the number is divisible by any integer within this range. This is a well-known optimization in prime checking, often termed the `Sieve of Eratosthenes`, which substantially reduces the number of iterations required to ascertain whether a number is prime. 

The second function, `prime_length(string)`, first validates that the input is a string and then uses the previously defined `is_prime` function to determine whether the length of the input string is prime.

This solution achieves a time complexity of `O(sqrt(n))` for checking the primality of a number, which is a highly efficient approach for this problem.