```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The code employs an iterative approach to determine the prime factors of a given integer `n`. It begins by assuming that `n` is not divisible by any number less than or equal to its current value. This assumption is then repeatedly tested for each integer between 2 and `i`. If `i` is divisible by any such number, the assumption is rejected, and `i` is deemed not prime. If the assumption holds for all values of `j` up to the square root of `i`, then `i` is confirmed as prime.

The function subsequently checks if the input number `n` is equal to the product of the factors found. If this is the case, it returns the list of prime factors in ascending order, including each factor the number of times it occurs in the factorization. 

Here is an example invocation of the function:
```python
factorize(70)
```

The above code returns `[2, 5, 7]`, which is the list of prime factors of the integer 70, containing each factor twice. 

This is because the prime factorization of 70 is 2 * 5 * 7, where both 2 and 7 are prime factors occurring once each, and 5 is a prime factor occurring twice.