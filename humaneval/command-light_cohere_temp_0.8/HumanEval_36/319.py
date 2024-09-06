```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        digit = str(num)[1]
        if digit == '7':
            count += 1
        if (num % 11 == 0) or (num % 13 == 0):
            count += 1
    return count

# Test the function
# Following are test cases to test the function
test_fizz_buzz = [('50', 7), ('78', 2), ('79', 3)]
for test, expect in test_fizz_buzz:
    actual = fizz_buzz(int(test))
    assert actual == expect, f"Error: {actual} != {expect}"
```

The function returns the number of times the digit 7 appears in the range of integers less than n which are divisible by 11 or 13.  The digit in the name of the function is chosen because it is the only number causing this behavior in this range. The function uses a number of times 7 appears to calculate the total.