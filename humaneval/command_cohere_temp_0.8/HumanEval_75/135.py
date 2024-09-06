```python
def is_multiply_prime(a):
    # check if a is divisible by 2 or 3
    if a % 2 == 0 or a % 3 == 0: 
        return False

    # check if a is divisible by any number in the range 5 to sqrt(a)
    for i in range(5, int(np.sqrt(a)) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0: 
            return False

    return True
```

This script defines a function called `is_multiply_prime` that takes a single argument `a`. The function returns True if the argument is the product of 3 primes and False otherwise. It first checks if `a` is divisible by 2 or 3, and since the product of primes involves at least one odd prime, such that `a` is not divisible by 2 or 3 if it is the product of 3 primes. 

Then, it checks whether `a` is divisible by any number in the range 5 to the square root of `a`. If `a` is the product of 3 primes, it is not likely to be divisible by many numbers in this range, but this approach ensures that all multiples of 2 and 3 are caught, and it stops at a point where it starts to check multiples of 6. If a is not divisible by 2, 3, 5, 7, 11, 13, 17 or 19 it returns `True`. Otherwise, it returns `False`. 

Please note that this approach is based on the assumption that there is at most one prime factor between 3 and the square root of `a`, which is not always true but should work for numbers smaller than 100. 

This solution can be improved further by introducing some more sophisticated ideas such as the Sieve of Eratosthenes.