```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(i) for i in range(1,n+1)) \
          <= 7 and n % 11 == 0 or n % 13 == 0

# Test it
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This code defines the fizz_buzz function that counts the number of times the digit 7 appears in integers less than n, which are divisible by 11 or 13, and returns 0 if the condition is met. The code then runs tests to check the function's correctness.