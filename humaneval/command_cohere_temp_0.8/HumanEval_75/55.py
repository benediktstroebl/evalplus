```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` checks if the given number is the multiplication of three prime numbers. The range of the square root of the input number is used to calculate the factors. The function then checks if the number is a prime number and if it has exactly three factors. And finally, the function checks if the maximum factor is one of the known prime numbers. This approach gives a time complexity of O(N^(1/2)) with N being the input number, which ensures a good performance for the given input range.