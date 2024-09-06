```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
    """
    factors = []
    for num in range(1, int(n**0.5)):
        if n % num == 0: factors.add(num)
    n //= int(n**0.5)
    factor = []
        while n % i == 0:
            factor.append(i)
            n //= int(n**0.5)
   
        i += 1
    return factor
# Example test
print(factorize(8))
print(factorize(25))
print(factorize(70))
```

This code defines a function called `factorize` which accepts an integer n as an argument and returns a list of prime factors of the given number in order. The function uses a loop to start from 1 and keeps checking divisibility until it reaches the square root of the number. It uses the while loop to find the prime factors and returns them in a list.

This function can be used to quickly find the prime factors of any given number, which is helpful for solving a variety of mathematical problems.