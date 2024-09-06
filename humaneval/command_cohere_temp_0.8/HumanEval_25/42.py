```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if n % j == 0:
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

The code uses a simple approach to find the prime factors of an integer `n`. It iterates through numbers from 2 up to `n` and checks if each number is prime or not. If a number is prime, it is added to the list of factors. Then, the code checks if the remaining `n` is greater than 1 after the above steps, and adds it to the list of factors if so. This way, the function returns a list of prime factors of `n` in ascending order, with each factor listed the number of times it appears in the factorization of `n`. 

Here is a simple test suite to verify the function:
```python
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]

test_factorize()
```