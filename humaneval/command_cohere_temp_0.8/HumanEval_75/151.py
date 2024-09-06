```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the prime factorization has exactly 3 factors
        return len(prime_factors(a)) == 3
    else:
        return False

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(int(n))
    return factors
```

The function `is_multiply_prime(a)` takes a number `a` as an input and returns `True` if `a` is the product of 3 prime numbers, and `False` otherwise. It achieves this in two main steps:
1. It uses the `prime_factors` function to retrieve the prime factors of the given number `a`.
2. Then it checks if the list of prime factors has exactly 3 elements. 

The `prime_factors` function loops over all the numbers from 2 to the square root of `n` and loops over each number in this range and checks if it is a prime factor of n. It adds each new prime factor to the list and divides `n` until it is either 1 or has only 2 residues. 

The proposed solution is sufficiently efficient with a time complexity of O(sqrt(n)) for the `prime_factors` function and O(1) for the main function, as it only applies the `prime_factors` once. Also, the `prime_factors` will likely be more efficient on average as it skips even numbers greater than 2. 

Note that the given example 30 would be false as 2 * 3 * 5 = 30 is not the product of 3 prime numbers. In fact, the only multiplication of 3 prime numbers less than 100 are the cubes of prime numbers: 2, 7, 13, 19, 23, and 31.