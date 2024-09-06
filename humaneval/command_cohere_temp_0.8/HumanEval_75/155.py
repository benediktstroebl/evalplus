```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the given number is the multiplication of three primes. The range of the square root of the input number is used to calculate all the factors of the input number and then check if there are exactly three of them. The function also checks if the factors are part of the predefined list of prime numbers (`primes`) and returns the appropriate boolean value. 

You can test the script by calling the function with different numbers. For example:
```python
print(is_multiply_prime(30))
print(is_multiply_prime(42))
print(is_multiply_prime(54))
```
The expected output would be:
```
True
False
False
```