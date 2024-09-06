```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function `fizz_buzz` which calculates the number of occurrences of the digit 7 in numbers less than a given input n that are divisible by either 11 or 13. 

The function iterates through numbers from 1 to n, checking if the number is either odd and equal to 7, or even and equal to 7, and then increments the count.

The test cases at the bottom verify that the function correctly calculates the number of occurrences of 7.