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
assert largest_divisor(8) == 4
assert largest_divisor(27) == 9
assert largest_divisor(100) == 10
```
This script defines the `largest_divisor` function and uses a loop to find the largest divisor of `n`. The loop starts from `i = 1` and goes up to `n`. It checks if `i` is a divisor of `n` and if so, it updates `j` with the largest divisor found, which is `n // i`. The loop returns the value of `j` if it's larger than `i`, or `i` otherwise. The function returns `1` if no number divides `n`. The tests assert the function behavior for different inputs.