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
```
This function uses trial division to determine whether a given number is prime or not. The function returns True if the is prime, and False otherwise. This can be tested through various test cases and passes them. The time complexity of the function is O(sqrt(n)).