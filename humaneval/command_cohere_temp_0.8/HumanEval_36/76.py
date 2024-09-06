Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases provided:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers less than n and divisible by 11 or 13
    counts = [
        count_seven(i) for i in range(n+1) if is_divisible_by_11_or_13(i)
    ]
    # Return the maximum count of 7 in the list
    return max(counts)

def count_seven(num):
    # Return the number of times the digit 7 appears in the integer num
    return num // 7 + (num % 7 > 0)

def is_divisible_by_11_or_13(num):
    # Return True if num is divisible by 11 or 13, otherwise return False
    return num % 11 == 0 or num % 13 == 0
```

The function count_seven(num) calculates the number of times the digit 7 appears in the integer num. The function is_divisible_by_11_or_13(num) returns True if num is divisible by 11 or 13, otherwise it returns False. These two functions are used within the fizz_buzz(n) function to determine the answer to the problem as per the given tests.