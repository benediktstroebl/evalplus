```python
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        m = int(math.sqrt(n))
        for i in range(2, m+1):
            if n % i == 0:
                factors.append(i)
                n = n // i
    return factors
```  This function, factorize, takes an integer n as input and returns a list of its prime factors in descending order. The function uses the process to find all the prime factors of the given number by checking for divisibility and using the concept of divisibility intervals.