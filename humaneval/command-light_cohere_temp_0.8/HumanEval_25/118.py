```python
def factorize(n):
    if n <= 1:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n ** 0.5) + 1, step=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    factors.append(n)
    
    return factors
```
The function `factorize` calculates the list of prime factors of a given number `n`. It initializes an empty list `factors` and then enters a `while` loop until the number becomes 1. In each iteration, it checks if the number is divisible by 2 and, if it is, it appends 2 to the list. If the number is divisible by a prime `i` starting from 3, it enters another `while` loop and appends `i` to the list. If the number becomes a prime factor, it returns the list of prime factors along with the final number.