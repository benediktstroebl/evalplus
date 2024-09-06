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

# Test the function with a markdown code block
**is_prime(6)**  # Returns False
**is_prime(101)**  # Returns True
**is_prime(11)**  # Returns True
**is_prime(13441)**  # Returns True
**is_prime(61)**  # Returns True
**is_prime(4)**  # Returns False
**is_prime(1)**  # Returns False
```
This function, **`is_prime`** takes an integer **`n`** as input and returns a boolean value indicating whether **`n`** is a prime number or not. The function employs several tests and algorithms to determine whether a number is prime or not, such as checking for divisibility by 2 and 3, checking for divisibility by prime numbers up to the square root of the number, and so on.