```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in number of times which it appears in factorization of given number
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n**0.5)+2, while n % num == 0:
        factors.append(num)
    n = n // num
    return factors
# test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This function factorize will return a list of prime factors in order from smallest to largest. It uses a while loop to check for all the prime factors of a given number until it becomes a prime number.