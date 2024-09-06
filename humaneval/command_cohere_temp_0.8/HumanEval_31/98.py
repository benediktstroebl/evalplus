Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning False if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns False. However, if it isn't, it returns True, indicating that the number is prime.

This implementation has a time complexity of O(sqrt(n)), which is efficient compared to a brute-force approach that would have a time complexity of O(n).

It handles edge cases like 1 and numbers less than 2 correctly, making its behavior consistent with the test cases provided.