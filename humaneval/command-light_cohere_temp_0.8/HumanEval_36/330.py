Here's the solution to the problem:
```python
def fizz_buzz(n):
    count = 0
    for i in range(2, n + 1):
        digit = str(i)
        if digit == "7" and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count
```

This code defines a function fizz_buzz that calculates the number of times the digit 7 appears in numbers less than n which are either divisible by 11 or 13. It uses a method to iterate through the numbers from 2 to n, checks if each number's digit is 7 and if the number is divisible by 11 or 13, and increments the count if both conditions are met. The function returns the value of the count, which represents the number of times 7 appears in such numbers.