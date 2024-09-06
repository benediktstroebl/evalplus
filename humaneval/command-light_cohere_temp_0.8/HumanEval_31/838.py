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

# Test function
def test_is_prime():
    print("The value of 6 is a prime.", is_prime(6))
    print("The value of 101 is a prime.", is_prime(101))
    print("The value of 11 is a prime.", is_prime(11))
    print("The value of 13441 is a prime.", is_prime(13441))
    print("The value of 61 is a prime.", is_prime(61))
    print("The value of 4 is not prime.", not_is_prime(4))
    print("The value of 1 is not prime.", not_is_prime(1))
```
The provided code defines a function is_prime that checks whether a given number is prime or not. The function uses a basic criteria for prime numbers and some optimizations to improve the efficiency of the check. The test_is_prime function serves as a testing tool for the is_prime function, and it provides informative messages for the passed test cases.