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

print('All tests passed!')
```

This script includes the 'is_prime' function, which is a basic check for primality. The 'count_up_to' function uses a simple loop to go through numbers from 2 up to `n`, adding each prime number to the `primes` list until the list has `n` elements. 

The script also includes a list of test cases to validate the functionality of the `count_up_to` function.  The `assert` statement checks that the output of the `count_up_to` function is correct for each test case. If the statements pass, the script outputs `All tests passed!`