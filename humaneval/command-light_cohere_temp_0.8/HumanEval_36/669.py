The following Python code demonstrates a self-contained function called fizz_buzz that efficiently counts the occurrences of the digit 7 in numbers less than a given input n and then only when those numbers are divisible by 11 or 13.

This function leverages a concise approach by utilizing list comprehension and the modulo operator. It efficiently filters numbers that meet the specific criteria and counts the occurrences of 7, providing a clear and efficient solution.

The fizz_buzz function is designed to be both readable and efficient, making it suitable for practical use cases where you need to quickly determine the frequency of specific digits in numbers divisible by 11 or 13. 

Here's the code:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Convert n to a list of integers less than n
    numbers = list(range(n, 0, -1))
    # Filter numbers that are divisible by 11 or 13
    divisible = [num for num in numbers if (num % 11 == 0 or num % 13 == 0)]
    # Count the numbers that are divisible by 11 or 13 and contain the digit 7
    count = sum(1 for num in divisible if num % 7 == 0)
    return count
```
This function can be used to quickly solve the problem for different input values, demonstrating the benefits of a self-contained, efficient, and readable function.