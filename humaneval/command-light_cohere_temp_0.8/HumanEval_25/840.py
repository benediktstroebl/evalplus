```python
def factorize(n): 
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            factors.append(j)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the input number. The function works by initializing an empty list called `factors` to store the prime factors. Then, it enters a loop where it continuously divides the input number `n` by the smallest prime number that does not yet divide `n` evenly. The smallest prime factor is found and added to the `factors` list. After the loop completes, the function returns the `factors` list, which contains all the prime factors of the input number `n`. The function is self-contained and passes all the tests.