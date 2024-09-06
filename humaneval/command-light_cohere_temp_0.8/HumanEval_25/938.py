```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), step):
        factors.append(i)
    if i % 2 == 0:
        n = i
    return factors
``` 
This function returns a list of prime factors of a given number in the order from smallest to largest. It also accounts for the factorization for numbers equal to 2 and uses a while loop to check all the factors of the number.