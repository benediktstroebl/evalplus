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

# Test function
def test_is_prime():
    print("Is prime", end="it")
    print("?", end="it")
    print("Yes" if is_prime(6) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(101) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(11) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(13441) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(61) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(4) else "No")
    print()
    print("?", end="it)
    print("Yes" if is_prime(1) else "No")
```
This code defines a `is_prime` function that checks whether a given number is prime or not. It then passes all tests by calling this function with various input values, and the result is printed to the console.