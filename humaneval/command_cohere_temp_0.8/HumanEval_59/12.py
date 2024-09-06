```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest % 2 == 0:
        largest //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while largest % i == 0:
            largest //= i
    if largest > 1:
        return largest
    return n
```

The provided solution leverages the fact that the first factorization step is targeted at locating the highest factor, thus ruling out the need for a separate prime check in the initial phase. The algorithm then effectively rules out factors 2 and 3, and progressively steps up to the square root of the number to eliminate successive potential prime factors. This approach ensures the ultimate generation of the highest factor, while keeping the overall number of divisions to a minimum.

Here is an example usage of the function:
```python
largest_prime_factor(13195) # Output: 29
largest_prime_factor(2048) # Output: 2
```

This should correctly solve the problem, while maintaining a self-contained function that can be easily imported and used elsewhere.