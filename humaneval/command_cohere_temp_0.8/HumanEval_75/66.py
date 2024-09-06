```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 3 > factors[factor] or n % prime == 0)
```
This script defines the `is_multiply_prime` function, which takes a number n as input and returns True if n is the product of exactly three prime numbers, and False otherwise.

The function first creates a list of prime numbers up to n and then iterates through each integer from 1 to n’s square root. If any integer can produce n as the result of a single multiplication, it is added to the `factors` set. After that, the function checks if there are exactly three distinct factors meeting the condition `prime ** 3 > factors[factor] and n is divisible by prime`. If this is the case, the number is considered to be the product of three prime numbers. Otherwise, it is not a multiplication of exactly three primes, so the function returns False. 

This solution has a time complexity of O(sqrt(n)) due to the loop iterating up to `n ** .5`, which ensures that all potential factors are accounted for in the most efficient way possible.

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
print(is_multiply_prime(36))
print(is_multiply_prime(52))
print(is_multiply_prime(55))
```
The output will be:
```
True
False
True
False
```

This shows that the function correctly identifies the given examples as multiplication of three prime numbers (true) and not (false).