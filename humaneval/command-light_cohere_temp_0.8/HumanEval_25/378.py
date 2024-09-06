```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    Python:
    if n < 2:
        return []
    # list all prime factors up to sqrt(n)
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, increment = 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(int(math.sqrt(n)) + 2, increment = i + 1):
        if n % i == 0:
            factors.append(i)
    return factors
```
This function employs the trial and error approach to discover the prime factors of the input number. It begins with the process by setting the variable 'factors' to an empty list. It then enters a loop while testing various numbers for divisibility, it adds the numbers to the 'factors' list as long as they are not divisible by the current value. The loop continues until it number becomes a prime number, at which point it will exit the loop and return the list of prime factors.