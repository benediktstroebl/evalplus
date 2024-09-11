```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(2, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script works by iterating over all integers from 2 to `n-1`. For each integer, it checks if it is divisible by 11 or 13 using the modulo operator (`%`). If it is, it converts the integer to a string and counts the occurrences of the digit '7' using the `count()` method. This count is then added to the total. The function finally returns the total count.