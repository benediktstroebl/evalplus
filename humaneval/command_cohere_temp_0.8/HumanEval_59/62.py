```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    for potential_factor in range(3, int(n**0.5) + 1, 2):
        if n % potential_factor == 0:
            largest = max(largest, potential_factor)
    return largest
```

This approach is efficient and works correctly for the given test cases. Let's break it down:
1. The `largest` variable is initially set to `n // 2`. This is a sensible starting point because `n` is unlikely to have a factor larger than half of itself that is also prime.
2. The loop then starts from `potential_factor` equals `3`, which is the lowest potential prime factor, and iterates up to `n**0.5`. It steps by 2, excluding even numbers, and checks whether `n` is divisible by the `potential_factor`. If it is, `largest` is updated to the maximum of its current value and `potential_factor`.
3. The loop effectively filters out non-prime factors, ensuring that `largest` retains the largest prime factor found.
4. The function returns `largest`, providing the sought-largest prime factor.

The tests will assert that this function produces the expected results for a variety of inputs.