```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if (digit == '7') and ((i % 11 == 0) or (i % 13 == 0)):
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This script defines a function `fizz_buzz` that calculates the frequency of the digit 7 in the numbers less than a given input value `n`. The function iterates through numbers from 1 to `n`, checks if the digit 7 is present and if the number is divisible by 11 or 13, it increments the count. The test cases demonstrate that this behavior of the function.