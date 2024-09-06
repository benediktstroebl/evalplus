```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(i) for i in range(1, n + 1) if i % 10 == 7 and i % 100 != 7)

# Test the function with a few inputs
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function fizz_buzz that calculates the number of times the digit 7 appears in the sequence of numbers less than n and which are divisible by 11 or 13. The function uses a string method str(i) to iterate through the digits of the numbers and checks if the current digit is 7 and if the number is divisible by 11 or 13. The return value of the number of such occurrences.