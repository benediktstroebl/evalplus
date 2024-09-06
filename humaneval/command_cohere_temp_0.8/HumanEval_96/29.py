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
    primes = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            primes.append(i)
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

for case in test_cases:
    assert count_up_to(case[0]) == case[1]
```

This script includes the 'is_prime' function, which efficiently checks if a given number is prime, and the 'count_up_to' function that uses the 'is_prime' function to solve the problem statement.

The 'test_cases' list contains input-output pairs to test the correctness of the implemented solution. The 'assert' statement checks if the output of the 'count_up_to' function is equal to the expected output for each test case.