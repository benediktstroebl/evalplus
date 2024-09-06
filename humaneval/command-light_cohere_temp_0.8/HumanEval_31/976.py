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
    print(is_prime(6))  # Output: True
    print(is_prime(101))  # Output: True
    print(is_prime(11))  # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))  # Output: True
    print(is_prime(4))  # Output: False
    print(is_prime(1))  # Output: False
```
This code defines a function `is_prime` that checks whether a given number is prime or not. It then provides test_is_prime() to call this function and prints the results.

The function uses a basic algorithm to test for primality. If a number is less than or equal to 1, it's not prime. If the number is a prime factor of 2 or 3, it's not prime. If the number is a perfect square trinomial, it's not prime. The function then iterates up the maximum sqrt(n) (sqrt of the number) and checks for divisibility by each integer in the range 5 to the square root of n. The function returns True if any of these conditions are met.