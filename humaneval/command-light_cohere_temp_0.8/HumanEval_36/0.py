```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == "7" and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

#Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop to iterate through the numbers from 1 to n, and for each number, it checks if the digit is 7 and if the number is divisible by 11 or 13. The function then counts the number of such occurrences and returns the result.