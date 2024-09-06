```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Return list is the factorization result.
    1) If number of 0's is the smallest prime factor
    2) If n is even, we start factorization from 2
    3) We find all prime factors of n
    """
    if n == 1:
        return []
    elif n < 2:
        return [1]
    else:
        for i in range(3, n // 2 + 1, 2):
            if n % i == 0:
                temp = i
                while n % temp == 0:
                    n //= temp
                    temp += 1
                else:
                    break
        return [temp] + [n] if n > temp else [n]

# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This code defines a function called `factorize` which takes an integer `n` as input and returns a list of its prime factors. The function uses a prime factorization algorithm to find the prime factors of the number, and the order of the factors is from smallest to largest in case of even numbers, and from largest to smallest for odd numbers.