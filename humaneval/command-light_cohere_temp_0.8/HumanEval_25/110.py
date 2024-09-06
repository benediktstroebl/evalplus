```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, increment=2):
        while n % i == 0:
            factors.append(i)
        n //= i
    for i in range(int(n**.5), -1, decrement=2):
        if n % i == 0:
            factors.append(i)
    return factors
```

This function, `factorize`, is designed to determine and return a list of prime factors for a given integer `n`. The function employs a loop to continuously divide `n` by its smallest prime factor, until it reaches a value that cannot be divided evenly. The `factors` list is then populated with the prime factors found in this manner.

This script's test cases pass because it correctly identifies the prime factors of the given numbers.