```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Get all digits in numbers less than n
    numbers = [i for i in range(10, n + 1, 1)]
    
    # Count occurrences of 7
    count = 0
    for digit in '0123456789':
        if digit in numbers and (digit != '7') & (numbers % 11 == 0 or numbers % 13 == 0):
            count += 1
    
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 

This function counts the number of times the digit 7 appears in the numbers less than `n` that are divisible by 11 or 13. It uses a Additionally learn faster by storing only the last digit seen in a number less than `n`.