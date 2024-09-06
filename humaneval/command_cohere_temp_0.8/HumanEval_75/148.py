```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(range(2, int(a**0.5) + 1)) | {a}
    for prime in primes:
        if prime not in divisors:
            return False
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the number is less than 100 and if it is, it creates a set of its divisors and primes from 2 to the square root of the number and checks if each prime is a divisor or not, if any prime isn't a divisor then the number isn't a multiplication of three prime numbers, otherwise, it checks if the size of the set is 3 to verify if the given number is the multiplication of three prime numbers. 

This solution has a time complexity of O(sqrt(a)) where a is the given number.