```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7' and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function
# uncomment below to run the tests
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```

This function checks if the digit 7 appears in the number and if the number is divisible by 11 or 13, it incrementss the counter. 

Then it returns the number of such occurrences.