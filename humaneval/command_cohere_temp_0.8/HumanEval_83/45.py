```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a variable to store the count of numbers that start or end with 1.
    count = 0
    # Count the numbers that start with 1
    if n >= 1:
        count += 9 ** (n - 1)
    # Count the numbers that end with 1
    if n >= 2:
        count += 9 ** (n - 2)
    return count
```

This Python script provides a self-contained function `starts_one_ends(n)` designed to address the problem of determining the count of positive integers that are `n` digits long, begin or end with the digit 1. The variable `count` is initialized to 0, and then the function calculates counts for numbers starting with 1 and ending with 1, respectively. The function adapts to numbers of different digit lengths by using the exponentiation operator `**` to efficiently calculate the counts for varying digit lengths, ensuring the accuracy of the result.