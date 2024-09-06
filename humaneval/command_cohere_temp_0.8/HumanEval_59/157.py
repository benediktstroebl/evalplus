```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2: 
        factors.append(n)
    return max(factors)
```
The function iterates through potential prime factors from 2 to `n**0.5`. It excludes even numbers apart from 2, as they would have already been factored out in the initial step. It then checks for divisibility by potential prime factors, iterating through numbers from 3 to `n**0.5` (excluding even numbers apart from 2). Once all factors are found, the function returns the largest one. 

This approach ensures identifying the largest prime factor while keeping the code efficient and concise.

This code snippet can be added to a Python script or integrated into a Python project to solve the given problem. It can also be executed directly in the Python interpreter to test it.