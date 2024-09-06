```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This script defines a function factorize that takes an integer n as input and returns a list of its prime factors. It uses a strategies like checking divisibility by 2, and dividing by divisors from 3 to the square root of n to find the prime factors of the number.

This function can be used to efficiently find the prime factors of any given number, which is a useful technique in number theory and other mathematical applications.