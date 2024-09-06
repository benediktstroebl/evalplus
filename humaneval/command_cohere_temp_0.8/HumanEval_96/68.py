Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n"""
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

The `count_up_to()` function iterates through integers from 2 up to `n`, it checks each integer with the `is_prime()` function, if it's prime and less than `n`, it adds it to the `primes` list and increments the `count` variable. Once the `count` reaches `n`, it breaks the loop to ensure it only collects the first `n` prime numbers.

You can test this function by calling `count_up_to()` with different values to verify it meets the requirements for each test case.