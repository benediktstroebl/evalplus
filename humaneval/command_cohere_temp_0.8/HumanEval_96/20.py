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

The `count_up_to` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime` function to verify if it's a prime number and if it's less than `n`. The `count_up_to` function collects these prime numbers in the `primes` list, and it stops collecting when the count of collected primes reaches `n` or exceeds `n`, whichever happens first. Test cases are provided to ensure the function behaves as expected.