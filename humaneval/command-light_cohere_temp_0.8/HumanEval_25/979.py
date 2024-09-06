```python
def factorize(n): 
    factors = []
    while n % 2 == 0: 
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, both odd:
        while n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(int(n**0.5) + 2, both even:
        factors.append(i)
    return factors
```

This function factorizes a given number n by finding its prime factors and returning them in list. The function first divides the numbers by 2 until the number becomes odd, then iterates through odd numbers to find the prime factors of the original number.