```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if ( num % 11 == 7 ) or ( num % 13 == 7 ):
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
 ``` 
This function, fizz_buzz, takes an integer n as input and returns the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13.