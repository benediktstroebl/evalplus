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

# Test case 1
print(is_prime(6))  # Output: False

# Test case 2
print(is_prime(101))  # Output: True

# Test case 3
print(is_prime(11))  # Output: True

# Test case 4
print(is_prime(13441))  # Output: True

# Test case 5
print(is_prime(61))  # Output: True

# Test case 6
print(is_prime(4))  # Output: False

# Test case 7
print(is_prime(1))  # Output: False
```
This Python function, `is_prime()`, determines whether a given number is prime. It first verifies if the critical factors for primality have been met. If the number is less than or equal to 1, it returns `False`. If the number is less than 3, it returns `True`. If the number is even or an odd number that can be expressed as 2n, it checks for divisibility by 2 and 3. It also checks if the critical factors are met, which include the square of the number being less than or equal to 2n + 1 and the square of the number being greater than 2n. If any of these critical factors are met, it returns `False`, indicating that the number is not prime. If none of these critical factors are met, it returns `True`, indicating that the number is prime.

Finally, the function performs a loop, using the square of the number as the loop condition. It squares the number and checks if the number is divisible by the result. If the number is divisible by the squared number or the result of adding 2 to the squared number, it returns `False`. If the number is not divisible by the squared number or the result of adding 2 to the squared number, it returns `True`, indicating that the number is prime.

The function is then tested with various input numbers, and the results are printed to the console. The test cases cover a range of possible inputs and ensure that the function correctly identifies prime and non-prime numbers.