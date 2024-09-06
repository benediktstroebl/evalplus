```python
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, :
        if n % i == 0:
            factors.append(i)
        n = n // i
    return factors

# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This function, `factorize`, takes an integer `n` as input and returns a list of prime factors of `n` in the order of their appearance. It uses a method to find prime factors by iterating through all the numbers from 2 up, checking if `n` is divisible by any of these numbers. 

The function does not require any additional data structures or external functions, and all calculations are performed in-house.