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
    result = count_up_to(case)
    assert result == expected, f"For input {case}, the expected result is {expected} but the actual result is {result}"
```

The script incorporates a function `is_prime(n)` that checks whether an integer is prime or not. 

The function `count_up_to(n)` takes an integer `n` and computes the first `n` prime numbers less than `n`. It uses a simple iterative approach, iterating through integers from 2 up to `n`, and adds each prime number to the `primes` list if it is less than `n`. The `count` variable keeps track of the number of prime numbers added to the list. Once the count reaches `n`, the function stops iterating and returns the `primes` list.

The last part of the code is a collection of test cases in the `test_cases` variable that are used to validate the correctness of the `count_up_to(n)` function. 

The script passes each `case` and `expected` result to the `count_up_to(case)` function and compares the result with the `expected` result. If they don't match, the code will throw an assertion error stating the difference between the actual and expected results.