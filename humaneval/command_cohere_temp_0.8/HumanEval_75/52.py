```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [divisor for divisor in primes if n % divisor == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the given number is the multiplication of three primes. It does so by initially creating a list of the first prime numbers. It then checks the divisors of the given number n, and finally, it returns true if the number has exactly three divisors, which means it's the multiplication of three primes. 

This solution has a time complexity of O(sqrt(n)) where n is the number given, as it checks the divisors of n, and for each prime, it takes at most O(sqrt(n)) steps to determine if it's a divisor or not.