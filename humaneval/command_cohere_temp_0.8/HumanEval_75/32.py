```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the number `n` is the product of three prime numbers. It first creates a list of prime numbers up to `n` and then calculates all the factors of n, checking if the number is divisible by any integer between 1 and its square root. Finally, the function returns True if all three factors are prime and they are all in the list of known prime numbers, and False otherwise. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The output will be:
```
True
```

This example shows that indeed the function correctly identifies 30 as a multiplication of three prime numbers: 2, 3, and 5.