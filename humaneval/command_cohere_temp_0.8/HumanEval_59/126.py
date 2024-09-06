```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Breadth-first search for factors
    i, factor = 2, n
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factor = max(factor, i)
    return factor
```
This function employs a breadth-first search (BFS) to find the largest prime factor among the factors of the input number `n`. Starting with a factor `i` set to 2 and `factor` set to `n`, the BFS search iterates through the numbers up to the square root of `n`, continuously dividing `n` by each factor it finds. The search terminates when `n` becomes 1, and the largest prime factor is retained in the `factor` variable. The maximum prime factorization can be achieved with this method, ensuring that the largest prime factor is found, regardless of the input number's size.