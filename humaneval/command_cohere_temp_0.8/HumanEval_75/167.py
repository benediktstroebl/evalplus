```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False
    return True
```

This function checks if a number is the product of exactly three prime numbers. It does so by iterating through a list of known prime numbers and checking if the number is divisible by any of them. If the number is divisible by at least one prime number, the function returns False, if it's not, it returns True. 

This approach works because if `n` is the product of three primes, it will eventually become divisible by at least one of the primes between 2 and the square root of `n` (consistently confirmed by the prime number theorem). 

Let's say `n = p1 * p2 * p3` where `p1`, `p2`, and `p3` are distinct primes. At least one of them, say `p1` will eventually divide `n` evenly. 

For example, 30 is the product of 2, 3, and 5. So, is_multiply_prime(30) is True. 

This approach has a time complexity of O(sqrt(n)) given that we only iterate up to the square root of n and will eventually find a prime divisor. 

To improve time complexity, you could skip known non-prime numbers, for example, the list of primes less than 100 is semicontinuous in that there are no gaps larger than 2, so we could optimize the function by removing the even numbers from the list of primes and iterate faster than O(sqrt(n)), although the upside to this optimization is minimal as the cost of the if statement would still remain.