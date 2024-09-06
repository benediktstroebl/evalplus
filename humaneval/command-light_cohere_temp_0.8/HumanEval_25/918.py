```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in factorization
    and the order is important! """ e.g. 2^4 goal
  providers list on it.
    list(range(2, int(n**0.0)+1))
    each integer divisible by n is dropped
    """
    factors = []
    for i in range(2, int(n**0.0)+1):
        factors.append(i)
    for j in factors:
        if n % i == 0:
            factors.remove(i)
    return factors
```
The function factorize returns the list of prime factors of the given number n, in the order from smallest to largest. The function works by iterating through the numbers from 2 to the square root of n, appending each number to the factors list if it is not divisible by n. The function then removes any numbers from the factors list that are divisible by n.