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

# Test the function with provided markdown code block tests
for test_num in markdown_tests:
    result = is_prime(test_num)
    if result:
        print(f"Yes, prime {test_num}")
    else:
        print(f"No, {test_num} is not prime")
```

This Python function, `is_prime(n)`, uses a simple and efficient algorithm to determine whether a given number is prime or not. It first handles small numbers, then checks divisibility by 2 and 3, and finally employs a 6-digit square root check to ensure the number is prime. The function then runs through the tests using a list of test numbers, and prints the appropriate message based on whether the number is prime or not.