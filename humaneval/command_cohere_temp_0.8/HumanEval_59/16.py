```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor
```

This approach iterates from 2 up to the square root of `n` (inclusive), and for each number, it checks whether the number is a factor of `n`. If it is a factor, it updates the `factor` variable to this value. After the loop, it returns `factor`.

#### Complexity Analysis:
Time complexity: O(sqrt(n))

This comes from the loop iterating through numbers from 2 to the square root of `n` (inclusive), and in the worst case, each iteration requires a linear operation to check the factorization.

Space complexity: O(1)

The space complexity is constant since the algorithm doesn't require any additional memory allocation or space that grows with the input size.