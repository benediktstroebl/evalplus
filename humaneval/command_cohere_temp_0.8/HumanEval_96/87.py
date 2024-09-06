Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime"""
    if n < 2:
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

This script defines a function `is_prime(n)` that checks if an integer is prime using a optimized iterative divisibility check from 2 to n's square root.

The main function `count_up_to(n)` iterates through integers from 2 up to `n`, adds integers that are prime (using the `is_prime` function) and less than n to a list `primes`. It increments a counter `count` and when it reaches `n`, it breaks the loop. Finally, it returns `primes`, which represents the first `n` prime numbers under `n`.

The test cases are defined and the function is tested against them. For each test case, the function is passed the expected result, and it is checked if the actual result matches the expected result.

The code includes necessary comments for readability and understanding.