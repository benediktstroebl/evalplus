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
The function 'is_prime' determines whether a given integer is prime. It does this by first determining if the number is less than or equal to one and returning 'False' in such cases. Then, it determines whether the number is even or odd and returns 'False' if it is even or odd, respectively. Next, it determines whether the number is divisible by 2 or 3 and returns 'False' in such cases as well. Finally, it determines whether the number can be expressed as a sum of consecutive primes (up to the square root of the given number) and returns 'False' if it can't be represented as such a sum and returns 'True' otherwise. The function also returns 'True' if the given number is greater than 3.