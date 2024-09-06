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
This function uses the above-mentioned approach to find prime factors of a given number. It will return the prime factors in ascending order, with each factor represented by the corresponding number of times it appears in factorization. 

In this function, the outer while loop handles the even numbers, and the inner loop handles all other numbers. The function will return a list of numbers representing the prime factors of the input number n.