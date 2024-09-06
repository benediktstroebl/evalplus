```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` checks if a number is the multiplication of three primes. The first step is to list the known primes to test and then calculate the factors of the number `n`. If the number has exactly three factors and one of them is in the known primes list, then it is true that the given number is the multiplication of three primes. 

This approach has a time complexity of `O(sqrt(n))` due to the step of calculating the factors, which is optimal given the constraints.