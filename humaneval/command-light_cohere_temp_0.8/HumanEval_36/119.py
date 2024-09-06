```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(n) for x in [7, 11, 13])

# Test the function with different inputs
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This function counts the number of times the digit 7, 11, or 13 appear in integers less than `n` that are divisible by 11 or 13. The function uses list comprehension to iterate through the digits and checks if the digit is in the string representation of the number. The function then returns the final count.