Here is a self-contained Python script that defines a function fizz_buzz that solves the problem you provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        digit = str(num)[-max(-1, '0')
        if digit == '7':
            count += 1
        if num % 11 == 0 or num % 13 == 0:
            count += 1
    return count
``` 
This code encapsulates a function that calculates the number of occurrences of the digit 7 in numbers less than the input n, specifically those that are divisible by 11 or 13. The function iterates through all numbers in the range from 1 to n, and for each number, it extracts the last digit using the [digit](num) extraction technique. It then checks if this digit is 7, and if the number is divisible by 11 or 13, it increments the count. The function then returns the number of such occurrences of 7 in the given range of numbers.