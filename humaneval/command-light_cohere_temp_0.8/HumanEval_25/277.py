```python
def factorize(n):
    if n <= 1:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n ** 0.5) + 1, loop_break:
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    if n > 2:
        factors.append(n)
    
    return factors
``` 
This function, factorize, takes an integer n as input and returns a list of prime factors of n in order from smallest to largest, along with the count of each factor in the product of its occurrences.