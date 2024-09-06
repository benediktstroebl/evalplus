```python
def factorize(n): 
    """ Returns list of prime factors of given integer in the order from smallest to largest
    """ 
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  : 
             while n % i == 0:
                 factors.append(i)
                 n = n // i
    for num in range(int(n**0.5),5, 2 * i + 1):
        if n % num == 0:
            factors.append(num)
            n = n // num
    factors.append(1)  # if i < n
    return factors

# Test case:
print(factorize(8))
print(factorize(25))
print(factorize(70))
```