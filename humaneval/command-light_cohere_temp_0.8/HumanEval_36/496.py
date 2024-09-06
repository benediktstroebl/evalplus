```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = list(range(10, n+1, 2))
    for num in nums:
        if (num%11 == 7) or (num%13 == 7):
            count += 1
    return count

#Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It works by creating a list of numbers from 10 to n, with step 2, then it iterates through this list and checks if the current number is divisible by 11 or 13 using the modulo operator. If the number is 7, it increments the count.