```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, by = 2):
        while n % i == 0:
            factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
This Python function called `factorize` takes an integer `n` as input and returns a list of its prime factors in descending order. The function first checks for a factor of 2 by dividing `n` by 2 and appending it to the `factors` list. Then, it iterates through all odd numbers from 3 to the square root of `n` with a step size of 2, and checks for divisibility by each number. If a number is found to be divisible by the current number, it is appended to the `factors` list. Finally, the last number in the list is the largest prime factor of `n`.