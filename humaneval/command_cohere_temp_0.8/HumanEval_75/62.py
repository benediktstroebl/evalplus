```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
    divisors = [num for num in prime_numbers if a % num == 0]
    return len(divisors) == 3
``` 

The function `is_multiply_prime` checks if the given number is the multiplication of three prime factors, it first assumes that the number has at least three distinct divisors and then checks if these divisors are prime.  If the condition is not fulfilled, it returns `False`, and if it is true, the function returns `True`. 

This approach results in a time complexity of O(sqrt(a)) for the case when the given number is composite and needs to check almost max divisor, but it turns to O(n) in the worst-case scenario when the number is prime, and it needs to check all prime numbers up to the square root of the given number. 

To improve the time complexity to O(log(a)), we can use the Sieve of Eratosthenes to pre-compute the primes and sort them in increasing order, so we can perform binary search on the array to find the potential divisors.  Here is an example: 

```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
    primes_sorted = sorted(primes)
    if len(primes_sorted) <= 3 * (a ** .5 + 1): 
        return False
    divisors = [num for num in primes_sorted[1:] if a % num == 0]
    return len(divisors) == 3
```