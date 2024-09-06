```python
def factorize(n):
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, i+=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```  This function uses a loop to find the prime factors of a given number and returns a list of the prime factors in order from smallest to largest.