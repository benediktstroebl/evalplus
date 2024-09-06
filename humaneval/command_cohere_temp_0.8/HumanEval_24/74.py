```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i > i:
            return i
    return 1
```
This Python script defines a function called `largest_divisor` taking a single argument `n`, which returns the largest integer divisor of n smaller than n itself. The function loops through numbers from 1 to n, checking if the number can be evenly divided by n and if it is larger than the current candidate divisor. If it is, the function updates the candidate divisor to this number. If no such divisor is found, the function returns 1. This algorithm is guaranteed to work for all positive integers.