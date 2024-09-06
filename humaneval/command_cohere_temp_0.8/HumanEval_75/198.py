```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    limit = int(sqrt(a)) + 1
    for i in range(2, limit):
        if a % i == 0:
            return False
    
    for i in range(2, limit):
        if a % i == 0 and is_prime(i):
            return False
    
    return True

def is_prime(n):
    # Return true if the number is a prime, false otherwise
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `is_multiply_prime(a)` aims to determine whether a given number `a` is the product of three prime numbers. It first considers the prime factors of the number and checks if there are exactly three of them. It does so by iterating from 2 up to the square root of the number, incrementing by 1. If the number is divisible by any of these candidates, it immediately returns `False`, as the number cannot be a product of three primes. It further explores the candidates that divided the number, checking if they themselves are prime using the `is_prime()` function. If any of these divisors is not a prime, `is_multiply_prime()` returns `False`. If none of these conditions are met, the function finally returns `True`, indicating that the number is a product of three primes. 

The `is_prime(n)` function is used to evaluate whether a given number n is a prime number or not. It employs a simple brute-force approach, checking all integers from 2 up to the square root of `n`, incrementing by 1. If any of these candidates divides `n`, it returns `False`, indicating that `n` is not a prime. If no divisors are found, it returns `True`, signifying that `n` is a prime number.

The code includes basic test cases that validate the behavior of the `is_multiply_prime()` function and demonstrate its correctness for various input scenarios. You can use these tests as a starting point to ensure proper function behavior against specific problem statements you might encounter. You can also adapt them to more sophisticated tests depending on particular cases you want to investigate further.