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
    res = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            res.append(i)
    return res

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

This Python script defines a function `count_up_to(n)` which takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The function uses a separate helper function `is_prime(n)` to determine whether a number is prime or not. The script also includes a list of test cases to validate the correctness of the `count_up_to(n)` function. 

The time complexity of `is_prime(n)` is `O(sqrt(n))` since it only checks up to the square root of `n`. The time complexity of `count_up_to(n)` is also `O(sqrt(n))` because it iterates from 2 up to `sqrt(n)`. 

Note that the `is_prime` helper function is deterministic but slightly slower than some prime-checking functions. However, because it only checks up to `sqrt(n)` it is vastly simpler than other prime-checking algorithms, and this simplicity makes it a good fit for clarity in explaining the problem.