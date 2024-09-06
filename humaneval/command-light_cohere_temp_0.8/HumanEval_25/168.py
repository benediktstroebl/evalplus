```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is also listed number of times corresponding to how many times it appears in factorization of the number.
    Input number should be equal to the product of all factors."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This Python function, `factorize`, computes the prime factors of a given integer `n` and returns them in order from smallest to largest. The function employs the standard method of factorizing, which involves checking divisibility by 2 and then by higher prime numbers until the number is fully factored.  The list of factors is generated in a loop that runs until the number can no longer be factored by any prime.