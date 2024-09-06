```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    count = 0
    primes = []
    for num in range(2, n + 1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

The `is_prime` helper function is implemented utilizing a streamlined primality-checking algorithm, which iterates through the integers from 2 up to the square root of the target number. This approach is more efficient than checking all divisors up to the target number. The `count_up_to` function uses the `is_prime` helper function to generate an array of the first `n` prime numbers less than `n`, which is then returned. 

This solution aims to balance simplicity, efficiency, and readability, and can be easily adapted to cater to more complex problems or optimized further if needed. 

```python
test_cases = [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (0, []),
    (1, []),
    (18, [2, 3, 5, 7, 11, 13, 17])
]

for case in test_cases:
    n, expected = case
    primes = count_up_to(n)
    assert primes == expected, f"For n={n}, expected={expected}, actual={primes}"
```

This test suite covers a variety range of scenarios, ensuring that the function correctly computes the prime counts for various input values.  If needed, the tests can also be expanded further to cover edge cases and other scenarios.  This will guarantee the robustness and adaptability required for handling more intricate problems.  Finally, the use of an efficient primality-checking algorithm guarantees that performance restrictions are kept to a minimum while solving this problem.  This will allow the solution to scale effectively for more complex scenarios.