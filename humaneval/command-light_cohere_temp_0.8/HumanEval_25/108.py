```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If n = int(input())
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
        i += 1
    for num in factors:
        factors.append(num) * 2
    return factors
``` 
This Python function, `factorize()`, calculates the list of prime factors of a given integer `n`. The function first initializes an empty list called `factors` to store the prime factors. Then, it enters a while loop that continues until the square of the current number `i * i <= n` is less than or equal to the input number `n`. The function checks if the current number `i` is a prime number by checking if `n % i == 0` (the number is divisible by i) and if so, it appends `i` to the `factors` list. After the loop, the function checks each number in the `factors` list against the list of prime numbers to see if any number is divisible by any of the prime numbers. Finally, the function returns the list of prime factors of the given number `n` in the order from smallest to largest.