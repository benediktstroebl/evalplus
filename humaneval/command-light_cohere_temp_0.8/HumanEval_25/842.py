```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
This script defines a function `factorize` that calculates and returns the list of prime factors of the given integer `n`. It uses a while loop to find all the prime factors, from smallest to largest, by continuously factoring out pairs of twos and then iterating up through prime numbers until the input number cannot be divided by any prime number.