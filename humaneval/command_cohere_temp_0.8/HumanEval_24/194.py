```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # banker's rule
            if j > i:
                return j
            elif i == j == n // i:
                return i
    return 1

# tests
assert largest_divisor(15) == 5
assert largest_divisor(18) == 9
assert largest_divisor(21) == 3
assert largest_divisor(27) == 9
```

This code defines the `largest_divisor` function, which iterates through all factors of `n` and returns the largest one that satisfies the problem's constraints. This approach covers cases where the largest divisor and the denominator of the resulting fraction are not the same. 

The test assertions ensure that the function behaves as expected for certain input values. Feel free to add more tests to cover other cases.