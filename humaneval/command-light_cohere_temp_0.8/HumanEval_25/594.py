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
``` 
This function uses the process of dividing by consecutive odd numbers to find prime factors. It then returns a list of the prime factors of the input number in ascending order.