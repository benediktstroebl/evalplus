```python
def factorize(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    return factors
```  This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a inner loop to check divisibility and adds the current prime factor to the list of factors until the number is no longer divisible by any previous prime factor.