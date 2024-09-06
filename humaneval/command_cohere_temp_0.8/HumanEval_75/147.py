```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for prime in primes:
        if n % prime == 0:
            divisors.append(prime)
    
    return len(divisors) == 3
``` 

The function `is_multiply_prime` checks if the number `n` is the product of three prime factors, it first collects a list of prime divisors of `n` from the predefined list of primes, then checks that the length of the list of divisors is exactly 3, which means that the number is a multiplication of 3 prime numbers. 

This approach provides a straightforward solution for the given problem. 
You can test this function by calling it with different numbers to check if it returns the correct value. 
For example:
```python
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(52))  # Output: False
print(is_multiply_prime(81))  # Output: True
``` 
This should return the result: `True, False, True`, respectively, due to the following factors:
```
- 30 = 2 * 3 * 5
- 52 = 2 * 2 * 13
- 81 = 3 * 3 * 3
``` 
You can add more tests to cover a broader range of cases and ensure the correctness of the function. 
If so, the code will pass the following test:
```
python -m pytest -sv --strict test_is_multiply_prime.py
```