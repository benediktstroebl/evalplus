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

# Test function to check if a given number is prime
def is_prime_test(n):
    return is_prime(n)

# Test array with some prime numbers and non-prime numbers
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for num in numbers:
    print(f"{num} is a prime {is_prime_test(num)}:")
```
This code defines a function called `is_prime` that checks whether a given number `n` is prime or not. It then defines a a test function `is_prime_test` that uses the `is_prime` function to check if a given number is prime. The code also creates an list of numbers, and then iterates through the list, printing out each number and its corresponding prime status.