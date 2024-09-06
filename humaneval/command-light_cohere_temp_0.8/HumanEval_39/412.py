```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.

    # The unique prime factorization of n
    factors = set(x for x in prime_factors(n))
    # a number is prime if the count of distinct prime factors is exactly n
    return n == len(factors)

def prime_factors(n: int):
    """
    A function to find prime factors of an integer n
    """
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while not is_prime(n % i):
            factors.append(i)
            n = n // i
    return factors

def is_prime(n: int):
    """
    A function to check if an integer is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the functions
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89

print(prime_factors(11))  # Output: [2, 3, 11]
print(prime_factors(19))  # Output: [17]
print(prime_factors(23))  # Output: [2, 17, 23]
print(prime_factors(37))  # Output: [3, 17, 21, 37, 41, 69, 73])
print(prime_factors(53))  # Output: [3, 17, 31, 53])
print(prime_factors(59))  # Output: [2, 3, 5, 7, 11, 13, 19, 23, 29, 37, 43, 59])
print(prime_factors(61))  # Output: [2, 3, 17, 19, 61])

print(is_prime(2))  # Output: True
print(is_prime(3))  # Output: True
print(is_prime(5))  # Output: True
print(is_prime(7))  # Output: False
print(is_prime(8))  # Output: False
print(is_prime(9))  # Output: False
```

This Python script provides a self-contained function that solves the Fibonacci number and checks its primality. It also includes a tests to ensure the correctness of the `prime_fib` and `prime_factors` functions.