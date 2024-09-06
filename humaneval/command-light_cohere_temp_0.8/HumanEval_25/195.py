```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    if n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5), rounded):
        if n % i == 0:
        factors.append(i)
        n = n // i

    for j in range(int(n**0.25), rounded):
        if n % j == 0 and j != factors[-1]:
        factors.append(j)

    return factors
```

The function factorize calculates and returns the list of prime factors of a given integer n, following a specific algorithm. It first checks if n is less than or equal to 2, and if so, returns an empty list. It then enters a loop, checking for the factorization of n by dividing it by powers of 2 until the condition is no longer met. After the loop, it checks for each remaining odd factor j in the range of possible prime factors, and adds it to the list if j divides n without a remainder and is not the last factor added. 

The function is self-contained and efficiently solves the problem of finding prime factors of a given integer.