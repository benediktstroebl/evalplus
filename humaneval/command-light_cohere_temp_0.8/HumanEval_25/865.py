```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors. The function first initializes an list to store the factors and then starts a while loop, where it checks if the number is even and, when it is, it appends the square of the number to the list of factors and continues dividing the number by squares until the square is larger than the input number. 
After the loop, if the number is still odd, it is a prime number and is the last factor. The function then returns the list of prime factors in the order from smallest to largest numbers.