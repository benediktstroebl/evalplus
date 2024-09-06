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

def test_count_up_to():
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

test_count_up_to()
```

This script defines a function `count_up_to(n)` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. It also has a function `is_prime(n)` that checks if a number is prime. Finally, it includes a test suite with the function `test_count_up_to()` to validate its behavior against various test cases.