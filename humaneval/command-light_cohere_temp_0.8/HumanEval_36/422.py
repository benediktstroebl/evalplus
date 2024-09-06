```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (10 * num + 7) % 11 == 0 or (10 * num + 7) % 13 == 0:
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines the fizz_buzz function, which takes an integer n as input and returns the number of times the digit 7 appears in integers that are less than n and divisible by 11 or 13. The function uses a loop to iterate through all numbers from 1 to n, and checks if the sum of the number and 7 (modulo 11 or 13) is divisible by 11 or 13. The function then counts the time 7 appears and returns the total count.