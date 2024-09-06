Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n."""
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

This script defines a function `is_prime(n)` that checks if a given number is prime. It then defines the function `count_up_to(n)` that takes an integer n and returns an array of the first n prime numbers less than n. The script also includes a list of test cases that verify the correctness of the code. 

The `is_prime` helper function is quite standard, but the `count_up_to` function uses an efficient strategy to find primes: it iterates through numbers starting from 2 and checks each number for primality using the `is_prime` helper function. Once it finds a prime, it appends it to the result list and continues counting. If the desired count is reached, it breaks out of the loop to stop at the right point.