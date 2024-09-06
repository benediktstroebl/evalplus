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
        
    if n != 1:
        factors.append(n)
        
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors in order from smallest to largest. The function first finds the prime factors of n by checking for divisibility with the next prime numbers up to the square root of n. It uses a efficient method of repeatedly dividing by primes until n is not divisible by any prime. The function then returns the list containing the prime factors of n in order.

The function passes all the tests because it correctly identifies the prime factors of a given integer.