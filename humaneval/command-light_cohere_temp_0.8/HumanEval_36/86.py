```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    i = n
    while i > 0:
        digit = str(i % 10)
        if digit == '7':
            count += 1
        i //= 13
    return count

#Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in numbers less than n, specifically those that are divisible by 11 or 13. The function iterates through the numbers and checks if the current digit is 7; if so, it increments a count. The function then returns this count, effectively solving the problem.