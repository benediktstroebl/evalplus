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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python function, 'is_prime(n)', takes an integer 'n' as an input and returns 'True' if 'n' is a prime number and 'False' otherwise. It first checks if 'n' is less than or equal to 1, in which case it is not prime. Then, it checks for the consecutive divisors: 2 and 3, returning 'True' if 'n' is divisible by 2 or 3. It then checks if 'n' is of the form 6k+1 or 6k-2, where 'k' is an positive integer less than 6. If 'n' is not of this form, it checks for divisors of 'n' using a while loop, ensuring that the loop only considers divisors less than the square root of 'n'. The function also handles the case when 'n' is 1, returning 'False'.