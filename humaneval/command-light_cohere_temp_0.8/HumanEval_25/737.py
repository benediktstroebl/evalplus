```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(int(n))
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n in order from smallest to largest. It uses a classic Sieve of Eratosthenes algorithm with slight modifications to improve efficiency for the base case n>2.

The function works by:
1. checking adding a requirement to append a new requirement that the current number can only be divided by itself and 1.
2. Generating a list of requirements.
3. Checking each of requirement and adding the corresponding factors to the list of factors
4. Generating the list of factors