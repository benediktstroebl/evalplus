```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the sqrt of a is an integer
        if int(sqrt(a)) == sqrt(a):
            # Split a into three factors
            factors = list(set(factorize(a)))
            if len(factors) == 3 and factors[0] * factors[1] * factors[2] == a:
                return True
    return False

def factorize(n):
    # List of primes starting from 2
    primes = [2]
    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        # Check the condition for primality
        if n % i != 0:
            primes.append(i)
    return primes
```

The function factorize, which is in charge of determining whether or not a given number is multiply prime, is encapsulated within the is_multiply_prime function in this code. The factorize function employs the divisibility rule to establish whether or not a number is prime.

A number is checked to see if it is less than 100 by the is_multiply_prime function. The factorize function is used to determine if the number has three distinct factors if it is. The number is multiplied by these three factors. The function returns True, indicating that the number is multiply prime if this is the case. The function returns False if the number cannot be divided into three distinct factors or if the square root of the number is not an integer.

You can use the is_multiply_prime function by providing an integer less than 100 as an input to determine whether or not the number is the product of three distinct prime numbers.

This solution has a time complexity of O(min(a, 100)) and a space complexity of O(min(a, 100)), where 'a' is the given number. It uses primality testing optimizations to efficiently determine if a number is prime.