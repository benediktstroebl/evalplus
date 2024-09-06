```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) //, while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
The function factorizes an input integer n by finding its prime factors. It first finds all even even factors of 2 by checking if n is divisible by 2. Then, it iterates through all prime numbers greater than 2 up to the square root of n, and checks if n is divisible by each prime number. If a prime number divides n, it is appended to the list of factors. The function returns a list of prime factors of n in the order from smallest to largest, with each factor number being listed number of times corresponding to how many times it appears in factorization.