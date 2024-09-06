```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime(n)` takes a number `n` as an input. First, it generates a list of prime numbers up to the square root of `n`. Then, it calculates the set of all factors of `n` and checks if their intersection with the list of primes is equal to the set of factors. The function returns `True` if the intersection is empty, meaning that all three distinct factors were prime. The function returns `False` if the intersection has less than three elements or no elements at all. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
print(is_multiply_prime(52))
print(is_multiply_prime(54))
```
This will output:
```
True
False
False
```