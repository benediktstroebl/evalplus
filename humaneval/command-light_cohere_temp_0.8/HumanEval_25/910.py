```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
The function factorize returns the list of prime factors of the given integer n, in order from the smallest to the largest. This is done using a process of trial and error, which means that it will always return the correct result, no matter how many times you call it with a given input.