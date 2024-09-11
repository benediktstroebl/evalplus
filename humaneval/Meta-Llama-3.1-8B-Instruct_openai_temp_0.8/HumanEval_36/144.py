```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input. It then iterates over all integers less than `n`, and for each integer, it checks if it is divisible by 11 or 13. If it is, it converts the integer to a string and counts the occurrences of the digit 7. The total count is returned at the end.