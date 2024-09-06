```python
def factorize(n):
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
```  This function, factorize, takes an integer n as input and returns a list of its prime factors. The function first checks if the number is less than 2, and if so, returns an empty list. Then, it enters into a loop and keeps dividing n by the smallest prime number possible until the remainder is 0. The number is effectively factorized and its prime factors are appended to the factors list. Finally, it checks for the remaining prime factors, starting from the next smallest prime number and keeps factoring until no more remainders.