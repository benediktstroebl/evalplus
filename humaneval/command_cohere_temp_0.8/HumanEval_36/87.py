Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases provided:
```python
def fizz_buzz(n):
    '''Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.'''
    # Define a list to store the results
    counts = [0] * (n + 1)
    # Initialize count at 0 for the count of 7
    counts[7] = 0
    # Find the count of integers divisible by 11 or 13 and less than n.
    for i in range(1, n + 1):
        if (i % 11 == 0 or i % 13 == 0) and i != 7:
            counts[7] += 1
    return counts[7]
```
This solution uses a simple iterative method to solve the problem. It loops through all the numbers below n, checks if the number is divisible by 11 or 13, and finally checks if the number is not equal to 7 to avoid overcounting. It then returns the count of 7 in the integers divisible by 11 or 13.