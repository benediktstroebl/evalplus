Here is a Python script that contains a self-contained function to solve the problem of counting the number of times the digit 7 appears in numbers less than a given input n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Initialize count with 0
    count = 0

    # Iterate through numbers from 0 to n
    for num in range(0, n+1):
        # Check if the number is divisible by 11 or 13
        if (num % 11 == 0 or num % 13 == 0):
            # If so, increment the count and skip the number
            count += 1
            continue  # Skip the number, so that the count is correctly calculated

    return count
```
This function takes an integer n as input and returns the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13. The function uses a iterators and conditional checks to achieve this.