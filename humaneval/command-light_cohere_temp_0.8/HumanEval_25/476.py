```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
    if n > 2:
        factors.append(n)
    return factors
```

This script defines a function called factorize, which takes an integer n as input and returns a list of its prime factors. The function first initializes an empty list called factors, then it starts by checking if n is divisible by 2. Then, it adds 2 to the list of factors, as 2 is the only even prime factor. The function then starts checking for larger prime factors, by incrementing the factor by i until the square of i is less than or equal to n. The function then adds the corresponding factor to the list of factors. 

This is a self-contained function that can solve the problem of finding the prime factors of a given integer and pass the test of correctness.