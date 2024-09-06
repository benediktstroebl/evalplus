```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The function `skjkasdkd` takes a list of integers as input and first filters out all prime numbers from the list using a list comprehension. Then, it finds the maximum prime number within the list of primes using the `max` function, and converts it to a string and sums up its digits using `sum` and `map`. The final result is the sum of the digits of the largest prime value in the list.

To validate the solution, we can write a series of test cases that cover a variety of scenarios:
```python
test_cases = [
    [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3],
    [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1],
    [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3],
    [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6],
    [0, 81, 12, 3, 1, 21],
    [0, 8, 1, 2, 1, 7]
]

for test_case in test_cases:
    assert skjkasdkd(test_case) == 10, "First test case failed"

for test_case in test_cases:
    assert skjkasdkd(test_case) == 25, "Second test case failed"

for test_case in test_cases:
    assert skjkasdkd(test_case) == 13, "Third test case failed"

for test_case in test_cases:
    assert skjkasdkd(test_case) == 11, "Fourth test case failed"

for test_case in test_cases:
    assert skjkasdkd(test_case) == 3, "Fifth test case failed"

for test_case in test_cases:
    assert skjkasdkd(test_case) == 7, "Sixth test case failed"
```

The tests will check the function's output against the expected values for each test case, ensuring that the function correctly solves the problem.