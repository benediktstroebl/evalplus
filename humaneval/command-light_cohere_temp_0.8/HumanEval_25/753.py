```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 2, while n % j == 0 and j != factors[-1]:
        factors.append(j)
    return factors
```
The function factorize takes an integer n as input and returns a list of its prime factors in descending order. 
It first checks for the factor of 2 and appends it to the factors list. It then checks for factors of larger than 2, starting from 3 and continues factoring until it finds all prime factors.  Finally, the function returns the list of prime factors.