```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n ** 0.5) + 1, step = 2**i
    while n >= step:
        factors.append(int(n // step))
        n = n // step
        
    factors.append(n)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a strategy of iterating through the numbers 2 to the square root of n, checking for divisibility. It factors out the a prime factorization by dividing n by each of these numbers, until n becomes a prime number or becomes smaller than the current step.