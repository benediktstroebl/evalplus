Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
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
    (18, [2, 3, 5, 7, 11, 13, 17]),
]
for case, expected in test_cases:
    assert count_up_to(case) == expected
```
The `count_up_to` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime` function to see if it's prime and if it's smaller than `n`, if so, it adds the number to the `primes` list and increments the `count` counter. When the counter reaches `n`, the function stops iterating and returns the list of prime numbers. 

The `is_prime` function is a simple primality test that checks if the number is less than 2 or if it has any divisors between 2 and the square root of the number. 

Finally, the test suite is included and it contains test cases that cover different scenarios like:
- `count_up_to(5) => [2,3]`
- `count_up_to(11) => [2,3,5,7]`
- `count_up_to(0) => []`
- `count_up_to(20) => [2,3,5,7,11,13,17,19]`
- `count_up_to(1) => []`
- `count_up_to(18) => [2,3,5,7,11,13,17]`