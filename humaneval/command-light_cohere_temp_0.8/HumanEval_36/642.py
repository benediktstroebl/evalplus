```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(n) for x in [7, 11, 13])

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13. It uses ass list comprehension to iterate through the digits of the number and checks if each digit is 7, 11, or 13. The function then returns the number of such digits.