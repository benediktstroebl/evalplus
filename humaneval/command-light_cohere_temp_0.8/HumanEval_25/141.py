```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(101)
    [2, 3, 5, 7, 11]
    >>> factorize(58005)
    [58005, 2, 2, 17, 53]
    """
    # Dividing by prime factorization to check if the number is prime
    if n == 1 or n == 0:
        return []
    elif n <= 1:
        return [1]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in factors:
        if j == 1:
            continue
        # Checking for larger prime factors
        k = j * i
        while k <= n and n % k == 0:
            factors.append(k)
        n = n // k
    return factors
``` 
The function uses a while loop to iterate through potential prime factors. It starts from the worst case of 3 and then checks for factors by multiplying the current prime factor with the previous prime factor, and so on. The function ultimately returns a list of prime factors of the given number, in order from smallest to largest.