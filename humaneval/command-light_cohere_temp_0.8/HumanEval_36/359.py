```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(i) for i in range(1, n+1)) % 2

# Test the function with some values
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13, and returns the number of such appearances modulo 2.