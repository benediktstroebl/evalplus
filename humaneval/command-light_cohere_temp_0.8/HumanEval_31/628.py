```python
def is_prime(n):
    """Returns True if n is a prime number, and False otherwise."""
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
```
This function uses a few basic rules to determine whether an input number is prime or not. It begins by testing numbers up to 3 and then iterates up to the square root of the input number, checking for divisibility with consecutive odd numbers and the input number itself. It also utilizes the time complexity of O(sqrt(n)). which is simple and effective, making it appropriate for this scenario.