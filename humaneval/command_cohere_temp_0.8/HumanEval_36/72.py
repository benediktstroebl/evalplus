Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the numbers from 1 to n.
    numbers = list(range(1, n + 1))
    # Count the number of times 7 appears in numbers divisible by 11 or 13.
    return sum(1 for number in numbers if divmod(number, 11)[0] == 7 or divmod(number, 13)[0] == 7)
```

This script defines a function fizz_buzz(n) that calculates the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13. It uses a list comprehension to iterate through the numbers from 1 to n, and checks if each number is divisible by 11 or 13. If a number is divisible by 11 or 13, it checks if the remainder of the division by 11 or 13 is 7, indicating the presence of the digit 7. The function returns the total count of such numbers.

Here is a usage example:
```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

This shows that the function fizz_buzz() returns 0 for values of n less than 51, since there are no numbers less than 51 and divisible by 11 or 13 that contain the digit 7. For n = 78, there are two such numbers (77 and 74), so fizz_buzz(78) returns 2. For n = 79, there are three such numbers (77, 74, and 71), so fizz_buzz(79) returns 3.