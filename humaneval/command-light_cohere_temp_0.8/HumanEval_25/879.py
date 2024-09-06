```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This Python function called factorize takes an integer n as input and returns a list of its prime factors. It does this by first checking for the number being even or not. If it's not even, it appends 2 to the list of factors. Then, it starts checking for the number being divisible by integers from 3 to the square root of n. The function iterates through these integers in increasing order, checks if n is divisible by each integer, and if so, appends the integer to the list of factors. Finally, it returns the list of prime factors.