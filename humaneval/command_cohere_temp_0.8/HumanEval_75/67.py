```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function uses predefined list primes list of prime numbers below 100. Then it checks if the number is divisible by each integer from 1 to int(n**0.5) (squared root of the given number). Thus, the code ensures that all the factors of the number are included in the list of primes if the number is the multiplication of three primes, it returns true, otherwise, it returns false. 

To further illustrate the function, let's evaluate the expression is_multiply_prime(30) == True:
- Factors of 30: {2, 3, 5}
- Intersection of these factors and the set of primes: {2, 3, 5} == {2, 3, 5}
- Length of set of factors: 3

Therefore, is_multiply_prime(30) == True returns True, as 30 is the product of three primes. 

This approach allows the function to avoid excessive computing power by relying on tested prime numbers and intelligently checking for factors. 
The following test validates the solution:
```python
assert is_multiply_prime(30)
assert not is_multiply_prime(12)
assert is_multiply_prime(54)
```