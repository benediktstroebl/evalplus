```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
# Add test cases to demonstrate the function
# test_factorize(8) gives [2, 2, 2]
# test_factorize(25) gives [5, 5]
# test_factorize(70) gives [2, 5, 7]
 ``` 
This function does prime factorization by dividing by 2 until the remainder is not equal to 0, then checking for all primes up to that divisor and adding them to the list of factors.