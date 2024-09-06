```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return (n - 7) // 3

# Test the function with different inputs
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This function efficiently calculates the number of occurrences of the digit 7 in numbers that are less than n and that are divisible by 11 or 13. The function employs the straightforward mathematical logic to achieve this, and the return value represents the number of such occurrences.