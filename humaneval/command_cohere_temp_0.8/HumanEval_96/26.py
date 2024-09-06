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
    assert count_up_to(case) == expected, f"For n={case}, expected {expected} but got {count_up_to(case)}."
```

The script includes a 'is_prime' function that efficiently checks if a number is prime. The 'count_up_to' function uses the 'is_prime' function to generate an array of prime numbers less than 'n' and returns the first 'n' primes if 'n' is a positive integer. Case handling for inputs like 0 and 1 is also included, returning an empty list as expected. Finally, the script validates the result through a list of test cases, ensuring correct behavior against given inputs. 

The 'is_prime' and 'count_up_to' functions are encapsulated in this code, providing a self-contained solution to the problem statement.