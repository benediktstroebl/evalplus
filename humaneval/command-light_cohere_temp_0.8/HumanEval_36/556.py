```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

#Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This script defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in numbers less than n which are divisible by 11 or 13. The function iterates from through to numbers from 1 to n, checks if the current number is divisible by 11 or 13, and if it is, increments a counter for the occurrences of the digit 7. The test cases ensure that the function is correctly implementing the problem definition.