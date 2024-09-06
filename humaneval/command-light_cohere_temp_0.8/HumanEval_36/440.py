```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-sub('0123456789', '7', 0, -1)]
        if digit == '7':
            count += 1
        if count == n:
            return n
    return count

# Test the function
for i in range(80):  # adding a large number n to increase the scope of the loop
    print(fizz_buzz(i))
```