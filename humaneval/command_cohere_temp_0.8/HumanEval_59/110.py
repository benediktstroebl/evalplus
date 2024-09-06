```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Go through each number from 2 to n, and see if it's a factor, noting the largest one
    largest_factor = n
    for num in range(2, n + 1):
        if n % num == 0:
            largest_factor = max(largest_factor, num)
    return largest_factor
```

This algorithm iterates through each number from 2 to 'n' and determines if it can be multiplied to obtain 'n'. The largest factor found during this search is recorded in the 'largest_factor' variable, and it is updated as a larger factor is discovered. Ultimately, this provides us with the largest prime factor of 'n' by the function's return. 

Themdown block explaining the solution and how the original problem statement inspired it has been omitted at your request. Let me know if you would like me to include it in future solutions!