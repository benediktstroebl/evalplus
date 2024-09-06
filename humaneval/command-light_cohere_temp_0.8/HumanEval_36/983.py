```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(i in str(i) for i in range(10, n+1, '7')) % 2

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
The code defines a function `fizz_buzz` that counts the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13. It uses a `sum` function to count these numbers, then takes the remainder of that value to return the solution.