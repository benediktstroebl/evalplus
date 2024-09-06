```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
            factors.append(n)
    return factors
```

This script defines a function `factorize` that takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a well backtracking method to find the prime factors of the number. The function first checks for the square of 2, and if the number is even, it adds 2 to the list of prime factors. The function then starts with i = 3 and iterates until the square of i is less than or equal to the number. The function checks if the number is divisible by i, and if it is, it adds i to the list of prime factors.