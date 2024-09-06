```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Make sure to include a docstring with the appropriate comment.
    # You can use the following hint to get started:
    # Consider using the factorization technique to find the largest prime factor.
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return max(factors)
```
The function largest_prime_factor(n) returns the largest prime factor of the positive integer n. To solve this problem, the factorization technique is used, where the number n is divided by each potential prime factor, starting from 2 and incrementing by 2 until the square root of n is reached. For each prime factor encountered, it is added to the factors list. The while loop ensures that n is divided exactly by the prime factor. After factorization, the maximum element in the factors list is returned, as it represents the largest prime factor of n. This approach efficiently finds the largest prime factor without the need for floating-point calculations or looping through individual integers.