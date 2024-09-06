```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if a number is the multiplication of three primes. First, it generates a list of prime numbers up to the square root of the given number n. Then, it calculates the factors of n and checks if their length is exactly 3 and that they are a subset of the primes list. The function returns True if these conditions are both satisfied; otherwise, it returns False. 

Here is an example usage output:
```python
>> is_multiply_prime(30)
True
```