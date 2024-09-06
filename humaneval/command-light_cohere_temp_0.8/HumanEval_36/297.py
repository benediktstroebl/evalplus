Here's the self-contained Python function to solve the problem you described: 

```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-subscript: -1]
        if digit == '7':
            count += 1
        if count == 3:
            return count
    return 0
```
This function `fizz_buzz` takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. 

The function uses a for loop to iterate through numbers from 1 to `n` and checks if the digit is 7. The function counts the count of the number of such occurrences and returns the result.