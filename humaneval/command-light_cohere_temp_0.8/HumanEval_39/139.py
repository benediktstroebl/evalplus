```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and is a prime if it's only divisible by 1 and itself.
    return (13 + (10 * (n - 1)) // (5 * (n - 2))
    while not ((10**9 + 7) // (5 ** n) <= 1):
        n -= 1
    return n

# Test case
def test_prime_fib(test_case):
    if isinstance(test_case, int) and test_case > 0:
        n = prime_fib(test_case)
        assert n == test_case
    return n == test_case

# Test cases
test_cases = [6, 7, 8, 9, 10, 11, 12]

for test_case in test_cases:
    print(f"Test case {test_case}:", end=" ")
    assert test_prime_fib(test_case) == test_case

```

This script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime by iterating until the number is "too big" This function then tests its functionality using the `test_case` and `assert` statements. The `test_cases` list contains a variety of test cases to pass. The test function uses the test_cases list to iterate through each test case and print out a message for each test case.