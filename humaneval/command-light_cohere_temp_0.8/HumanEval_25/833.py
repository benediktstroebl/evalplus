```python
def factorize(n): 
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1: 
        if n % 3 == 0:
            factors.append(3)
            n = n // 3
        elif n % 5 == 0:
            factors.append(5)
            n = n // 5
        elif n % 7 == 0:
            factors.append(7)
            n = n // 7
        else:
            factors.append(int(n % i for i in range(11, 64, by(1)))
        factors.sort()
    print(factors)
```
This function identifies and returns the list of prime factors in the order from the smallest to the largest, using the method above and making sure the output is sorted.