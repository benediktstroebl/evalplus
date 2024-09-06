Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through integers from 2 up to `n`, it checks each integer with the `is_prime()` function. If it's a prime number and less than `n`, it's added to the `primes` list. The loop stops when `count` reaches `n` or when `n` has been exceeded. 

To efficiently check if a number is prime, the `is_prime()` function iterates through integers from 2 to `sqrt(n)` and checks if the number is divisible by any.

You can test this script by calling the `count_up_to()` function with different values for `n` and verifying that it returns the expected list of prime numbers.