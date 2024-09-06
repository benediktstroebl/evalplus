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
    numbers = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            numbers.append(i)
            count += 1
            if count == n:
                break
    return numbers
```
The `count_up_to()` function takes an integer `n` as input and creates an array of the first `n` prime numbers less than `n`. The `is_prime()` function is used to efficiently determine if a number is prime. The loop starts from 2 and iterates up to the square root of the current number `i`, checking for divisibility. If a number is not divisible by any integer within this range, it is considered prime. 

Here is a test drive suite that can be used to verify the functionality of the `count_up_to()` function for various inputs:
```python
test_suite = [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (0, []),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (1, []),
    (18, [2, 3, 5, 7, 11, 13, 17])
]

for n, expected in test_suite:
    numbers = count_up_to(n)
    assert numbers == expected, f"For n={n}, expected={expected}, actual={numbers}"
```
This test drive suite covers various scenarios described in the problem statement.