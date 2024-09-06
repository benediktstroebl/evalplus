```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # Check if n-1 and n-2 are both primes
        if prime_fib(n-1) and prime_fib(n-2):
            return n
        else:
            # Try all prime factors of n
            factor_n = []
            for i in range(2, int(n**0.5) + 1):
                while n % i == 0:
                    factor_n.append(i)
            if len(factor_n) > 1:
                    return n
                else:
                    return 0
```