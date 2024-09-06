```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n = n // i
            else:
                i += 1
    return factors
# Driver code
test_factorize = [25, 100]
print(factorize(test_factorize[0]))  # [ [5, 5], [2, 4]]
print(factorize(test_factorize[1]))  # [2, 4, 8, 16]
 ```  This code defines a function called `factorize` which takes an integer n as input and returns a list of its prime factors. The function uses a iterative method to find the prime factors of n, starting from 2 and moving up as long as the square of the number becomes smaller than the number.