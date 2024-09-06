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

This approach first exhausts the even factors, then moves through the odd factors starting from 3, repeatedly dividing n by each prime factor it finds. Once the while loops exit, any remaining value in n is a prime factor not yet accounted for, which is appended to the list. Finally, max() returns the largest factor. This solution is efficient in terms of time and space complexity, O(sqrt(n)) and O(n) respectively. It should reflect well in tests like 2048 and 13195. 

Please let me know if you'd like me to explain any part of the solution or provide further insights on optimizing prime factorization!