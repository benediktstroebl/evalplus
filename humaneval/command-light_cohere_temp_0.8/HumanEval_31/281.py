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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```  This code defines a function **`is_prime(n)`** that checks whether a given number is prime or not. It uses a basic primality checks ( divisibility by 2 and 3, and the sqrt protection for small primes), followed by an efficient square root check for larger primes up to the square root of the input number. 

The function then is tested on a range of numbers, and the output is printed to verify its correctness.