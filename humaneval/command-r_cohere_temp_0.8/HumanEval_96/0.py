```python
def count_up_to(n):
    primes = []
    for num in range(2, n + 1):
        # simple optimization, skip middle five numbers,
        # since they are unlikely to be prime
        if num % 2 == 0 or num % 5 == 0:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes
```