Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
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

This script defines a function `count_up_to(n)` that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n. The `is_prime()` function is used to check if a number is prime. The script also includes a series of test cases to validate the correctness of the `count_up_to()` function. 

You can copy and paste this code into a Python interpreter or script to test it yourself. Feel free to modify or expand on this code to further explore the concept of prime number generation and usage.