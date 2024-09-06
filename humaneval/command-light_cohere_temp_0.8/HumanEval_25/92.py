```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        for i in range(3, int(n**0.5/5, n // i):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Example
print(factorize(8)) # [2, 2, 2]
print(factorize(25)) # [5, 5]
print(factorize(70)) # [2, 5, 7]
 ``` 
This script defines a function `factorize` which returns a list of prime factors of a given integer `n`. The function uses a loop to check for divisibility by 2 and then iterates through the numbers 3 to the square root of `n` checking for divisibility by each number.  The function then returns a list of the prime factors found in the order from smallest to largest. 

Note that you can use this function to pass any integer to solve the problem for that integer.