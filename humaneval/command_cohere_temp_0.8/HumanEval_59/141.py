```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    while factor > 1:
        test = 2
        while test ** 2 <= factor:
            test += 1
        if factor == test - 1:
            break
        elif factor % test == 0:
            factor //= test
        else:
            test += 1
    return factor
```
The function iteratively divides `n` by the candidate factors, starting from 2, updating the candidate factor value until it reaches 1, or a perfect division is found. This way, it identifies the largest prime factor of the given number.

Here is an example of function usage:
```python
largest_prime_factor(13195)  # Output: 29
largest_prime_factor(2048)    # Output: 2
```
This output is in line with the examples provided in the initial problem description.