```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest. """
    def prime_factors(x):
        factors = []
        while x % 2 == 0:
            factors.append(2)
            x //= 2
        for i in range(3, int(x**0.5) + 1, while x % (i) == 0:
            factors.append(i)
            x //= i
        for i in factors:
            while x % i == 0:
                x //= i
        return factors
# test cases
print(prime_factors(8)) # [2, 2, 2]
print(prime_factors(25))# [5, 5]
print(prime_factors(70))# [2, 5, 7]
``` 
The code defines a function called `factorize` which takes an integer n as input and returns a list of its prime factors. The `prime_factors` function is used to find the prime factors of a given number, it does this by iteratively dividing the number by its divisors until it becomes a prime. 

The test cases section demonstrates the function by passing different numbers to the `factorize` function and printing the resulting list of prime factors. 

This approach has a time complexity of O(sqrt(N)), as it uses the trial and error algorithm to find the prime factors.