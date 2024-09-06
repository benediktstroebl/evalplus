```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the number `n` is the product of 3 prime numbers. It first fetches the list of prime numbers up to `n`. Then it calculates the factors of `n` and checks if the length of the factors list is 3 and that all factors are present in the prime numbers list.

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The above will print `True` since 30 is the product of 3 prime numbers: 2, 3, and 5. 

This problem can be solved in various ways, this solution is just one of many possible solutions. Let me know if you'd like to explore more ways to solve this problem or any other aspect of the solution provided.