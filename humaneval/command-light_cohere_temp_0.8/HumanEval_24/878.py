Here is a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) //divis(n, i):
        factors.append(i)
    factors.sort(factors)
   return max(factors, key=lambda x: x[0])
```
This function is self-contained, and it can be used to find the largest divisor of any given positive integer number.