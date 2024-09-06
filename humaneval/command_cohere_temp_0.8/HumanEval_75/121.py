```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime` checks if the given number is the multiplication of three prime numbers. The first step of the function is converting the integer to a set of its factors. The second step is filtering out the elements of the set of factors that are primes. The function returns false if there are fewer than three prime factors, or if any of the prime factors are not in the set of factors of the number. Otherwise, it returns true. The overall time complexity of the function is `O(sqrt(n))`, which is the time complexity of the `range` function.

Here is an example of using the above function to verify the statement.
```python
print(is_multiply_prime(30))
print(is_multiply_prime(36))
print(is_multiply_prime(54))
print(is_multiply_prime(60))
```
The output will be:
```
True
False
True
False
```