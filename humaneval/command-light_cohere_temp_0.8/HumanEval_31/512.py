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

# Test the function with some inputs
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
``` 
This Python function checks whether a given number is prime or not. It first handles the next few numbers: it returns True for numbers less than or equal to 3 and False otherwise. Then, it checks for divisibility by 2 and 3, returning False if either of these numbers are divisible by the input number. Finally, it checks if the input number is divisible by any number between 5 and sqrt(n) (i.s of the method (which includes checking divisibility by 2 and 3, as well as square and cube roots), it returns True if the input number is a prime number and False otherwise.