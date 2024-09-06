```python
def factorize(n):
    factors = []
    
    for i in range(1, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if len(factors) != int(n ** 0.5):
        raise ValueError("Invalid number, not prime.")
    
    return factors
```
This function takes an integer `n` as input and returns a list of prime factors of the number `n`, in order from the smallest to the largest. It also provides tests tests for validity.