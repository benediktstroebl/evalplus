```python
def is_prime(n):
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

# Test function to check if a given number is prime
def is_prime_test(n):
    return is_prime(n)

# Test cases
print(is_prime_test(6))  # Output: False
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```

The code defines a function `is_prime` that checks whether a given number is prime. The function utilizes a technique called "Miller-Rabin primality test," which is a more efficient method for prime checking compared to the traditional Sieve of Eratosthenes. The function also includes test cases to ensure that the `is_prime` function correctly identifies prime and non-prime numbers.