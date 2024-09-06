```python
def largest_prime_sum_of_digits(nums):
    primes = [i for i in nums if is_prime(i)]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

The function `largest_prime_sum_of_digits()` takes a list of integers (`nums`) as input and applies the `is_prime()` function to determine the list of prime numbers within the list. The function then returns the sum of the digits of the largest prime number among those found. The `is_prime()` function checks whether a given number is prime or not, returning True if it is, and False otherwise. It employs a combination of conditions and iterative checks to efficiently determine primality. 

This solution focuses on determining the largest prime number within the list and calculating the sum of its digits, as required by the problem statement.