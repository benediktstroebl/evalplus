Here is a self-contained Python function that checks if a given number is a prime:
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

This function uses a combination of divisibility testing and trial division to efficiently determine whether a given number is prime or not. It follows the basic and secure guidelines for prime number checking, making it suitable for a variety of real-world applications.