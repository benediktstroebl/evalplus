```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
```  This function takes an integer n as input and returns a list of its prime factors in ascending order, with an optional condition to handle big numbers.  The output is a list of numbers, each corresponding to how many times its corresponding factor appears in the factorization of the original number.