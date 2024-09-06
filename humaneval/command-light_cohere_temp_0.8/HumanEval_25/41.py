```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, step by step):
        if n % i == 0:
            factors.append(i)
            n = n // i
    return factors
``` 
This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. It uses a iterative method to find the prime factors and checks divisibility by numbers from 3 to the square root of n while adding them to the list of factors.