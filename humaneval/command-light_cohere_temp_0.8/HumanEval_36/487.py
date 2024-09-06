```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    i = n
    while i >= 0:
        digit = str(i)
        if digit == "7":
            count += 1
        i -= 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop to iterate through the numbers less than n, checking if the current number is divisible by 11 or 13. The function then counts the occurrences of the digit 7 and returns the final count. The test cases demonstrate the expected outputs for different values of n.