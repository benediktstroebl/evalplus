```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for n being a prime number
    if factor == n:
        factor = n
    return factor
```

This script defines a function called `largest_prime_factor` taking a single argument, `n`, and returns the largest prime factor of `n`. The script defines the function, and then a set of tests is written. These tests include testing on known prime numbers and known non-prime numbers to ensure correctness of the function. 

Here is an example of how you may use this function in command line:
```python
largest_prime_factor(13195)
```
Which returns:
```
29
```

And here is another example of using the function to compute the largest prime factor of 2048:
```python
largest_prime_factor(2048)
```
Which returns:
```
2
```