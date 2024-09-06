```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(range(2, int(a ** 0.5) + 1)) | {a}
    for prime in primes:
        if prime not in divisors:
            return False
    return not any(divisor == a for divisor in divisors)
```

This function first creates a list of prime numbers up to `a` and then checks if each prime is a divisor of `a`. The function returns false if any prime number is not a divisor of `a`, and true otherwise. 

Here is a more concise implementation using the same logic:
```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if a % prime:
            return False
    return len(set(range(2, int(a ** 0.5) + 1)) & set(map(lambda x: a // x, primes))) == 3
```

To get a true result for the given example, a larger prime list should be used:
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```