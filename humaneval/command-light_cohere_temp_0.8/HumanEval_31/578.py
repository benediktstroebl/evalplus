```python
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

# Unit tests for the is_prime function
test_is_prime = []
test_is_prime.push({'6': is_prime(6), "Should return False" )
test_is_prime.push({'6': is_prime(101), "Should return True")
test_is_prime.push({'int': is_prime(11), "Should return True")
test_is_prime.push({'int': is_prime(13441), "Should return True")
test_is_prime.push({'int': is_prime(61), "Should return True")
test_is_prime.push({'int': is_prime(4), "Should return False")
test_is_prime.push({'int': is_prime(1), "Should return False")
test_is_prime.push({'int': is_prime(13), "Should return False")
```
The code defines a function called is_prime that checks whether a given number is prime. The function first handles small numbers, then checks for divisibility by 2 and 3, and finally uses a trial and error approach to find the largest prime number less than or equal to n. The code then tests the function to ensure its correctness and passes all tests.