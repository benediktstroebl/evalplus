```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i
    return 1  # return 1 if no number divides n

# Tests
assert largest_divisor(15) == 5
assert largest_divisor(7) == 1
```
This code defines the `largest_divisor` function, which iterates through all numbers from 1 to `n` and checks if they divide `n` without a remainder. The largest such divisor smaller than `n` is returned, and if no number fits this condition, the function returns 1. The tests assert that the function behaves as expected for two different input values.