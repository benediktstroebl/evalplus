```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    # Loop through each each number and see if it's divisible by any integer in range from 2 to sqrt(n). 
    # If it is, we add it to factors list.
    factors = []
   
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n ///2** if i == 2)
            return factors
    """

# Example test cases 
print(factorize(8))
print(factorize(25))
print(factorize(70))
```
The function factors out each prime factor by iterating from 2 to the square root of n. This is the order, which is the most efficient way to find prime factors of a number. The function returns a list of prime factors in ascending order.