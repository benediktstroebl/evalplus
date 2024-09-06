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

The function `largest_prime_sum_of_digits()` takes a list of integers as input and calculates the sum of the digits of the largest prime number in the list. To do this, it first finds the list of prime numbers using the `is_prime()` function, provided by the user. The `is_prime()` function checks if a number is prime or not, iterating through numbers up to the square root of the number and checking for divisibility. Once the list of primes is found, we return the sum of the digits of the largest prime, which is the maximum prime saved beforehand.  The function is designed to handle cases where the list contains no prime numbers, returning 0 in such cases.  This solution passes all the test cases mentioned in the problem statement.