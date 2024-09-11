```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The input integer to be factorized.
    :return: A list of prime factors.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we start by dividing the input number `n` by the smallest prime number, which is 2. If `n` is divisible by 2, we divide it and add 2 to the list of factors. We continue this process until `n` is no longer divisible by 2. Then we move on to the next number, 3, and repeat the process. We only need to check up to the square root of `n`, because if `n` has a factor larger than its square root, it must also have a corresponding factor smaller than its square root. This is why we use the condition `i * i <= n` in the while loop. If `n` is a prime number greater than 1 at the end of the loop, we add it to the list of factors.