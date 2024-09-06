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
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
        if count == n:
            break
    return primes

# Tests
test_cases = [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (0, []),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (1, []),
    (18, [2, 3, 5, 7, 11, 13, 17])
]

for case, expected in test_cases:
    actual = count_up_to(case)
    assert actual == expected, f"For n={case}, expected {expected} but got {actual}"
```

The code provides the `count_up_to` function to solve the problem and the `is_prime` function to check if a number is prime. The `count_up_to` function loops through numbers from 2 up to `n`, it checks each number if it's prime using the `is_prime` function, if it's prime and less than `n` it's appended to the primes list. The `count` is incremented each time a prime is found and when it reaches `n`, the loop is stopped so that the primes list has the first `n` prime numbers under `n`.