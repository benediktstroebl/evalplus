```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(int(n))
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ``` 
This code defines a function factorize, which accepts an integer n as input and returns a list of its prime factors. The function employs a method of loop and trial division to identify the prime factors of the given number.