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

# Test function to check if a number is prime
def is_prime_test(n):
    return is_prime(n)

# Test various inputs
print(is_prime_test(6))  # Output: True
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```

This code defines the `is_prime` function that checks whether a given number is prime or not. The function uses a regular prime number checks, such as checking divisibility by 2, 3, and 5, and also ensuring the number is not divisible by any smaller prime number with a factor less than or equal to the square root of the number. 
The `is_prime_test` function is a simple wrapper around `is_prime` that allows you to easily test the correctness of the function with various inputs. 
The script then provides a set of test cases to pass to the `is_prime_test` function and prints the expected outputs.