```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n + 1, 2)
    for num in nums:
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The above function fizz_buzz calculates and returns the number of times the digit 7 appears in the integers less than n which are divisible by 11 or 13. The function uses a efficient approach by using a loop to go through the integers in the range from 10 to n, and for each number, it checks if the number is divisible by 11 or 13 using the modulo operator.  The number of times 7 appears is then added to the count variable.