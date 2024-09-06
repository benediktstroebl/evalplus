```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    i = 4  # i is always going to be 4, 8, 11, 14, ...,etc.
    while n >= 4:
        if n % 10 == 7:  # If n is 7, add 1 to count
            count += 1
        n //= 4
    return count

# Test the function
for i in range(80):
    if fizz_buzz(i):
        print(i, end=' ')
```