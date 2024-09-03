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

This approach first checks if `n` is even and accordingly updates the list of factors. It then iterates through odd numbers and repeatedly divides n by each prime factor it finds. Finally, if `n` is still greater than 2, it is appended to the list of factors. The function returns the maximum factor from the list. 

This ensures that the code efficiently identifies the largest prime factor, while maintaining a clear and concise structure. Let me know if you would like to further discuss any part of the solution or clarify any additional problems you may have.