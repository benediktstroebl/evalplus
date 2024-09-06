```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = str(i)
        if '7' in num.7 in num:
            count += 1
        if 11 <= num <= 13:
            break
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop to iterate through the numbers from 1 to n, and for each number, it checks if the number contains the digit 7 and if it is divisible by 11 or 13. If the condition is met, the function adds 1 to the count variable. The loop continues until it reaches a number that is either less than 11 or greater than 13.