```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if a given number is the multiplication of three primes. It first calculates the factors of the number and then checks if there are exactly three of them and that they are also in the list of known prime numbers (`primes`). 

This approach allows the function to achieve a good performance while being able to verify if a given number is the multiplication of three primes in constant time. 

Note that the function assumes that the input is less than 100, as mentioned in the prompt. You can adapt it to your needs, possibly removing this assumption, and adapting the code accordingly, especially regarding the handling of prime numbers.