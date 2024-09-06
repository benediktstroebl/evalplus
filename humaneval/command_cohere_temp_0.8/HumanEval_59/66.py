```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
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
This approach first divides the number by 2 until it becomes odd. Then it iterates through odd numbers from 3 up to the square root of n, dividing n by each prime factor it finds. The last factor left, when n is finally 1, is the largest prime factor. The max operation is used to ensure that the largest factor is returned, just in case the number is divisible by 2 more than once.