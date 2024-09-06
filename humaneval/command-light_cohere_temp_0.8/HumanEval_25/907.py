```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    if n > 2:
        factors.append(n)
    
    return factors
```
This function computes the prime factors of the given integer n. It uses a loop to find all the prime factors, including the number itself, in the factors list. The loop starts from 2 and moves up to the square root of n while checking for divisibility. Once the loop is complete, any remaining number cannot be a prime factor, so it is added to the factors list.