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

# Test function to check if a number is prime
def test_is_prime(n):
    if not_prime(n):
        return n
    else:
        return False

# Test list of numbers to check
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in numbers:
    print(f"{num} is prime: {test_is_prime(num)}")
```
The above code defines a function that checks whether a given number is prime or not. It uses a testing to ensure the correct behavior of the is_prime() function.