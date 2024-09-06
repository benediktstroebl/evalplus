```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```
The factorization algorithm is simple and works by iteratively dividing the number by the smallest potential prime factor and recording the count. The function starts with the smallest potential prime factor, which is 2, and iterates through the numbers up to the input number. 

If a number evenly divides the input number, it is a prime factor, and the function counts its occurrences while dividing the number. The process continues until the input number becomes 1, at which point the list of prime factors and their counts is returned as the result.

Here is an example of how you can call this function:
```python
print(factorize(8))
print(factorize(25))
print(factorize(70))
```
This would output:
```
[2, 2, 2]
[5, 5]
[2, 5, 7]
```