```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
This Python script defines a function called `largest_divisor` taking a single argument `n`, which returns the largest integer divisor of n smaller than n itself. The function loops through numbers from 1 to n-1, checking for each number if it can divide n evenly (i.e., the result of n % i is 0). If such a number `i` is found, the function returns i. If no such number is found, the function returns 1. This approach is efficient because it takes advantage of the fact that any divisor of n smaller than n can only be 1, 2, ..., n-1, due to the limited range of testing.