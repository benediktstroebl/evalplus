```python
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
        else:
            i += 2
    return factors
# Example usage:
print(factorize(8))
print(factorize(25))
print(factorize(70))
```
This function factorizes a given number n and returns a list of its prime factors. The loop starts by checking if 2 divides n, if it does, it's added to the list of factors. If not, the function starts a "friends" approach, where it iterates through the numbers i, i*i, and i*2i, looking for numbers that divide n.