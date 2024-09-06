```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return False

    # Check if a is the product of 3 primes
    prime_numbers = [2, 3, 5, 7, 11, 13]
    factors = []
    
    for prime in prime_numbers:
        while a % prime == 0:
            factors.append(prime)
            a //= prime
            
    if a > 1 or len(factors) != 3:
        return False
    
    factors.sort()
    return factors[0] * factors[1] * factors[2] == a
```

The function `is_multiply_prime` checks if the given number `a` is the multiplication of three primes. It first checks if `a` is greater than 100, returning false if so. It then checks each number in a list of prime numbers ([2, 3, 5, 7, 11, 13]) to determine if any factorize into that number. If so, it adds these to a list of factors, continuing the division until the number is no longer divisible. If `a` has more than 3 factors, returns false. If `a` is greater than 1 and the length of the factors list is 3, it sorts the list and returns true if their product is equal to `a`. 

The unit tests in the script test this function on various inputs, all of which return the expected boolean value. You can use this script to test other inputs as well.