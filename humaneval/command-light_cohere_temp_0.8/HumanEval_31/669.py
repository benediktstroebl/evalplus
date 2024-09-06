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
This code defines a function called `is_prime` that checks whether a given number is prime or not. The function uses a basic primality tests and returns True if the number is prime and False otherwise. The tests include checking for divisibility by 2 and 3, as well as checking for divisibility by numbers that are the sum of two consecutive odd numbers. The function also performs a specific test that checks if the square of the number is less than or equal to 4. The test stops if the square is less than 4, and returns True if the condition is met. If the condition is not met, it returns False.