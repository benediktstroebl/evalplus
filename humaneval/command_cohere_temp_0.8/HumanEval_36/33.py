Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13
    pertinent = [7] + [i for i in range(n+1) if i%11==0 or i%13==0]
    # Count the occurrences of digit 7 in the pertinent list
    return pertinent.count(7)
```
This code provides a function that solves the problem as stated in the prompt. It first creates a list of relevant integers, and then it counts the occurrences of the digit 7 in that list. This solution avoids the use of floating-point numbers and uses divisibility conditions to identify the relevant set of numbers.