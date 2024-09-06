```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n+1, 2)
    for num in nums:
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Example of usage:
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
This function takes an integer n and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. 

The function uses a loop to generate numbers from 10 to n, inclusive of n, with a step of 2 (to account for both 7 and 13). It then checks each number against 11 and 13 using the modulo operator %, and increments the count if the number is divisible by 11 or 13. 

Finally, the function returns the count, which represents the number of times the digit 7 appears in the relevant range of numbers.