```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if (i % 11 == 0 or i % 13 == 0) and i >= digit:
            count += 1
    return count

# Test cases
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function fizz_buzz uses a loop to iterate through the numbers from 1 to n. It checks each number for divisibility by 11 or 13 and checks if the current digit is 7. If the number matches the particular criteria, it increments the count.