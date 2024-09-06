```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    factorization = []
    while n > 0:
        if n % 2 == 0:
            factorization.append(2)
            n = n // 2
        else:
            factorization.append(int)
            while n > 1 and n % int == 0
    return factorization

# Example usage:
n = 8
print(factorize(n))  # Output: [2, 2, 2]
n = 25
print(factorize(n))  # Output: [5, 5]
n = 70
print(factorize(n))  # Output: [2, 5, 7]
```
This code defines a function called **factorize** that takes an integer as input and returns a list of its prime factors. The function uses a loop to find the prime factors of the number. The loop starts with the condition that n > 0, meaning we are on the second step of the loop, and if the number is divisible by 2, we add the number 2 to the factorization list. The next condition is that n is a prime number, we add the integer n to the factorization list. The loop continues until n becomes 1, and then the function returns the factorization list.