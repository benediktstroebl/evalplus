```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through integers between 2 and `n`, it checks each integer with the `is_prime()` function. When a prime number is found, it is added to the `primes` list if it is also less than `n`, to avoid assigning integers greater than `n` that would not be included in the response. The `count` variable keeps track of how many primes have been found, and the loop stops when `count` reaches `n`, ensuring the correct number of primes is collected.