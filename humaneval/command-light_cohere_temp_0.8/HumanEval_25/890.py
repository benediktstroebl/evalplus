```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n = n // i
    return factors
#example
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This function takes an integer `n` as input and returns a list of its prime factors in order, from smallest to largest. It uses a simple strategy of checking for divisibility by 2 and for numbers greater than 2, it checks for divisibility by numbers that are at least 3 times the square root of `n` and divides `n` by these numbers iteratively until it becomes 1.