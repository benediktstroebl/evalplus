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
# Run the function to test it
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This code defines a function factorize, which takes an integer n as input and returns a list of its prime factors. It uses a run this function on three test cases and prints the resulting list of prime factors.