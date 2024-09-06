```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization of the given number.
    Input number should be equal to the product of all factors"""    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n ** 0.5) + 1, j <= int(n ** 0.41)  and n % j == 0:
        factors.append(j)
    return factors
```
This function returns a list of prime factors of the given number in order from smallest to largest. It uses the same loop to find all factors and appends them to the `factors` list. The loop starts from 2 and goes up to the square root of the number. Finally, it checks for factors less than the square root of the number and adds them to the list if they are factors.