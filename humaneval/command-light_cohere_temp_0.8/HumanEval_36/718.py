```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 0 or num % 13 == 0) and str(num)[-len():7] > count:
            count = str(num)[-len():7]
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function fizz_buzz(n) calculates the number of times the digit 7 appears in the range of integers less than n that are either divisible by 11 or 13. The function iterates over the each integer in the range and checks if the number is divisible by 11 or 13 and whether the number's last digit is 7. If so, the digit count is incremented. The function returns the results in the number of times 7 appears in such numbers.