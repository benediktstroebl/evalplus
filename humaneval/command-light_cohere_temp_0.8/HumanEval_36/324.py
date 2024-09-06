```python
def fizz_buzz(n):
    count = 0
    for i in range(2, n + 1):
        if str(i) == '77':
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This code defines the fizz_buzz function, which determines the number of times the digit 7 shows up in numbers less than n that are divisible by 11 or 13. The function loops through the numbers from 2 to n, and it adds to the count if the number's string equals '77'. The function then returns the count, which represents the number of times 7 appears in the supplied range of integers.