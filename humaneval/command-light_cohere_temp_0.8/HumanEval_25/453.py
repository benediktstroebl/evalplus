```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function uses a loop to find the prime factors of a given number. It starts by checking for divisibility by 2 and adds it to the list of factors. Then, it iterates through numbers from 3 to the square root of the original number, checking for divisibility while dividing by each number. The function also handles the case where the number is already a prime by not appending it to the list of factors.