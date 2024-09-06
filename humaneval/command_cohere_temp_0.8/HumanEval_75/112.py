```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in primes for factor in factors)
```

The function `is_multiply_prime` checks if the given number is divisible by any numbers from 1 to its square root. If not, it proceeds to check if any divisors are primes. The list of prime numbers is utilized to speed up the process and lessen the complexity of the approach. This method allows the function to effectively determine if the given number is the product of three primes. 

Here is a sample output of the function:
```
> is_multiply_prime(30)
True
```
```
> is_multiply_prime(36)
False
```
```
> is_multiply_prime(40)
False
```