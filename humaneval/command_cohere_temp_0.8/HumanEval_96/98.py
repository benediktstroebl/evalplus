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

This script defines a function `is_prime(n)` that checks if a number is prime using the divisibility rule. It then defines the function `count_up_to(n)` that takes an integer `n` as input and returns the first `n` prime numbers less than `n`. The script also includes a list of test cases that verify the correctness of the `count_up_to` function. 

To ensure the function behaves correctly for edge cases, we include tests with `count_up_to(0)` and `count_up_to(1)` to verify that the function returns an empty list for cases where `n` is 0 or 1 as prime numbers are undefined in these cases. 

The `count_up_to(n)` function iterates through numbers from 2 up to `n`, it checks each number if it's prime and if so, it appends it to the primes list if it's less than `n`. The `count` variable ensures we only append `n` primes to comply with the problem's request.