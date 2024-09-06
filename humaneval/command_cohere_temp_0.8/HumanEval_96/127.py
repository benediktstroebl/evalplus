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
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            primes.append(num)
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

This script defines a function `is_prime(n)` that checks if a given number is prime. It then defines the function `count_up_to(n)` that takes an integer n and returns an array of the first n prime numbers less than n. The `count_up_to(n)` function iterates through integers from 2 up to `n`, it keeps track of the count of prime numbers and when the count reaches `n`, it stops. The `is_prime(n)` function is used to check if a number is prime. The script also includes a list of test cases to validate the correctness of the implemented function. 

The provided test cases cover different scenarios and ensure that the function `count_up_to(n)` produces the expected results. You can add more test cases to cover a broader range of input scenarios and corner cases to verify the full functionality of the solution.