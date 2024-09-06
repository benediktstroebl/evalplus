```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum = 0
    for i in range(1, n+1):
        digit = ord('7') + (i - 1)
        if (str(format(str(i), '10.0'))[0] == digit):
            if (i % 11 == 0 or i % 13 == 0):
                sum += 1
    return sum
``` 
This script defines a function, fizz_buzz, which calculates the number of times the digit 7 appears in the range of integers less than a given number n, specifically those that are divisible by 11 or 13. The function uses a loop, iterating over integers from 1 to n, and for each number, it checks if the corresponding digit is present in the number's decimal representation (converted to a string using str()) and also if the number is divisible by 11 or 13. If both conditions are met, the digit is added to the sum. The function returns the sum after the completion.