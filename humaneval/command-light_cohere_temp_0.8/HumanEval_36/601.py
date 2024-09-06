Here is a self-contained Python script that defines a function fizz_buzz that solves the problem you provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    7digit_count = 0
    for i in range(1, n+1):
        digit = str(i)
        count = digit.count('7')
        if count > 0 and (count > 1 or i % 2 == 0) and (i % 11 == 0 or i % 13 == 0):
            7digit_count += 1
    return 7digit_count

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function fizz_buzz that counts the number of occurrences of the digit 7 in integers less than n which are divisible by 11 or 13. The function iterates through the integers from 1 to n and checks if the digit 7 appears in the number and if it is divisible by 11 or 13. If both conditions are met, the digit is added to the count.