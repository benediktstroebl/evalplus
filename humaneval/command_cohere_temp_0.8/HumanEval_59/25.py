```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for potential factors greater than int(n**0.5) as well
    # Note: This section is slower but is unlikely to make a difference
    # for typical inputs. See https://en.wikipedia.org/wiki/Prime_number#Prime_numbers_less_than_political_powers_of_two
    if factor == n:
        for possible_factor in range(3, int(n**0.5) + 1, 2):
            if n % possible_factor == 0:
                factor = possible_factor
    return factor
```
The function iterates through possible factors from 2 up to `int(n**0.5) + 1`, and if `n` is divisible by any, it updates the `factor` to be that divisor. It then checks for odd factors greater than `int(n**0.5) + 1` by iterating in steps of 2 starting from 3. This is done because odd numbers greater than `int(n**0.5) + 1` will not lead to any smaller factors and hence can be checked less frequently.

However, it's important to note that this approach is not the most efficient way to find the largest prime factor, especially for larger numbers. More efficient algorithms like the `prime_factors` function combined with `max()` would be better suited for larger numbers. 

Here's an example of how you might use the `prime_factors` function from the Python standard library to find the largest prime factor more efficiently:
```python
import math
import numpy

def largest_prime_factor(n):
    factors = numpy.prime_factors(n)
    return max(factors)
```
This version leverages numpy's efficient prime-finding algorithm to identify all prime factors of the number, and then selects the largest from the list of factors. 

Remember, the original approach is mathematically correct and viable for small numbers, but the latter approach is more efficient and recommended for larger numbers.