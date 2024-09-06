```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(2, int(n**0.5) + 1, while n % (j**2) == 0 and j != i:
        i = j
    return factors
# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This function factorize calculates and returns a list of prime factors of the given integer n. It uses a simple algorithm that iterates through the numbers from 2 to the square root of n, checking for divisibility and keeping track of which factors have been found so far. The list of prime factors is returned in the order of increasing size, from smallest to largest.