```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first initializes an empty list called `factors` to store the factors. Then, it enters a `while loop` that continues until the number becomes even. 

The function then appends the current prime factor `2` to the list of factors. The function then divides the number by 2 and updates the variable `n` to be the quotient. 

Finally, the function returns the list of prime factors found for the number `n`.