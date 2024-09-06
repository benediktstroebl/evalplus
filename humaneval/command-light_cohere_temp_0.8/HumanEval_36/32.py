Here is a self-contained Python script with a function that solves the problem of counting the number of times the digit 7 appears in integers less than a given number n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int(str(i)[-0])
        if digit == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function with n = 50, n = 78, and n = 79
# Test the function with a range of numbers
for i in range(50, 79):
    print(fizz_buzz(i), end=' ')
``` 
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13. The function uses a `count` to keep track of the number of such digits. The function then iterates through the numbers from 1 to `n` and checks if the digit at the 0th index of the string representation of the number is 7. If the digit is 7 and the number is divisible by 11 or 13, the count is incremented. The function returns the number of such times the digit 7 appears in such numbers.