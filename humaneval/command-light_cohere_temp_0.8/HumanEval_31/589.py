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

# Test the function with provided markdown code block
is_prime(6)  # Should return False
is_prime(101)  # Should return True
is_prime(11)  # Should return True
is_prime(13441)  # Should return True
is_prime(61)  # Should return True
is_prime(4)  # Should return False
is_prime(1)  # Should return False
``` 
The function `is_prime` checks if a number is prime or not. It follows a basic algorithm of checking divisibility up to sqrt(n) and then every multiple of 6 until the number becomes prime.