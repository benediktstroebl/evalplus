```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    # Each of the factors should be listed number of times corresponding to how many times it appers in factorization.
    # Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    factors = []
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        if i != int(n**0.5):
            break
        return factors
    else:
        # The last non-trivial factorization step is not 2, so it's odd.
        factors.append(n)
    factors[int(len(factors)) - 2]
```
This function factorizes a given number into a list of prime factors in a specific order. The function handles the following:
 - If the input number is less than or equal to 1, it returns an empty list.
 - If the input number is even, it has only one factor, which is 2, so it returns [2]. Then, it recursively factorizes the number by dividing by 2, and the process continues until the next odd factor is found. 
 - If loop starts iterating from 3 and checks if the number is divisible by the current factor. Once the loop finds a factor, it adds it to the list of factors and breaks out of the loop. 
 - If loop adds all factors it finds to the list and breaks out of the loop.