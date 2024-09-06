```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors

# Test the function
print(factorize(8))
print(factorize(25))
print(factorize(70))
 ```

This code defines a function called factorize that takes an integer n as input and returns a list of its prime factors. The function uses a while loop to find all the prime factors of the number, starting from 2 and going up to the square root of n. The function also uses a for loop to find all the prime factors of the number, starting from 3 and going up to the square root of n.