Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    less_than_n = [int(x) for x in range(n - 1, 1, -1)]
    return sum(1 for x in less_than_n if x % 11 == 0 or x % 13 == 0 and 7 in str(x))
```
This code defines a function fizz_buzz that calculates the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It accomplishes this by iterating through integers less than n and testing for the conditions of divisibility by 11 or 13 and the presence of digit 7. The sum function is used to count the occurrences and return the result.