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
This function, `is_prime`, uses a basic algorithm to determine whether a given number is prime. It starts by checking numbers less than or equal to 2 and 3 since they are prime. It then uses a specific condition to check for divisibility by 2 and 3, and then employs a simple while loop to keep incrementing the loop condition until the square root of the number exceeds the number.