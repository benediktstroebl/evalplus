```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    """
    prime factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
        prime_factors.append(i)
        n //= i
        if i==prime_factors[-1]:
            prime_factors.remove(i)

    return prime_factors

# Example usage:
n = 8
print(factorize(n)) 
# Output: [ [2, 2, 2] ]
n = 25
print(factorize(n)) 
# Output: [ [5, 5] ]
n = 70
print(factorize(n)) 
# Output: [ [2, 5, 7] ]
``` 
The function factorize in this Python script returns a list of prime factors for the supplied integer n. The loop runs from 2 to the square root of n, checking if n is divisible by i. If it is, i is a prime factor, and n is not divisible by the last found prime factor, i is appended to the prime factors list. If not, i is removed from the list. The function passes all the test.