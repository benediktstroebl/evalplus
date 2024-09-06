```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n //= i
    for num in factors:
        if num > 1:
            nums = []
            while n % num == 0:
                n //= num
                nums.append(num)
            factors.append(nums)
        return factors
``` 
This function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The factors are determined using a trial and error method, with special cases handled and optimized for efficiency.