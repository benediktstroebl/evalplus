```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors
```
This Python function, factorize, calculates the list of prime factors of a given integer n. The function first initializes an list called factors to store the prime factors. Then, it starts a loop while the given number n is not divisible by 2, it adds 2 to the list of factors. In the inner loop, the function checks if the number is divisible by i, where i ranges from 3 to the square root of n, plus 1. The function then divides n by i and adds i to the list of factors if the condition is satisfied. Finally, the function returns the list of factors.