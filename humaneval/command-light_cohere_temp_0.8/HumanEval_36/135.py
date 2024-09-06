Here's a self-contained Python function that solves the problem of counting occurrences of the digit 7 in numbers less than n and passing the test of the function:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        num = str(num)
        count += num.contains('7')
   
    return count
```