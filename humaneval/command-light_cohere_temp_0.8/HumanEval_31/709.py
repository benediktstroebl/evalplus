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
```
The function `is_prime(n)` determines whether a given number is prime. It follows a well series of tests: checks for divisibility by 2 and 3, then checks for divisibility by numbers forming the hypotenuse. It also checks divisibility by numbers that are equal to the square of the number being tested, starting from 5 and increasing the value of the square by 6 each time the number being tested is less than the square number of the tested number.