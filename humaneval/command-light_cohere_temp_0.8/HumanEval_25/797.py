```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in the factorization of the number
    Input number should be a product of all its factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 1, while n % (i**2) == 0 and i != factors[-1]:
        factors.append(i)
    n = n // i
    for j in factors:
        factors.append(factors[0].5] * j //
        factors.append(factors[0].5] * j)
    return factors

```  The function first initializes an empty list, then it keeps track of the factors it has found. It then starts by checking if the number is even or odd. If the number is even, it adds the number itself to the list. If the number is odd, it then checks all the prime numbers from 3 to the square root of n. The function then checks if the number is divisible by any of these prime numbers. If it is, it adds the number to the list. The function then keeps iterating until it finds a number that the number is divisible by.  Finally, the function returns the list of prime factors of the original number.