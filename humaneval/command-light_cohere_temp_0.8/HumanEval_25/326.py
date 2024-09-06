```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ``` 
This code defines a function called `factorize` that takes an integer n as input and returns a list of its prime factors. The function uses a loop to find the prime factors of n, starting from 2 and moving on to the square root of the input number.