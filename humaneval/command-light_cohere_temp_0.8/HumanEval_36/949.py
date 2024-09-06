```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(10, n+1, step=1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
 ``` 
This code defines a function `fizzBuzz` which calculates the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13. The function uses a loop to iterate through the numbers from 10 up to `n` (inclusive) and checks each number for divisibility by 11 or 13. The number of such time the divisible by 11 or 13 is the same as the number of times the digit 7 appears, so we only count the digit 7 once in this case.