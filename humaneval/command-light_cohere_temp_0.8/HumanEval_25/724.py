```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
```  This function takes an integer n and returns a list of its prime factors in order, from smallest to largest. The function first adds 2 to the list if n is even, then it iterates through the numbers from 3 to √n.  The function checks if n is divisible by each number in this range and appends the number to the list if it is divisible by that number.