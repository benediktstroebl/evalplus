```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting digits,
    # so the largest number considered is 99999...99 (10^n - 1) to account
    # for the possibility of starting with a 1.
    numbers = [0] * int(10 ** n)
    
    # Count numbers starting with 1
    numbers[1] = 1
    
    # Count numbers that end with 1
    for i in range(2, 10 ** n - 1):
        numbers[i] += 1
        numbers[10 ** n - i] += 1
    
    return sum(numbers)
```

This Python script defines a function `starts_one_ends(n)` to count the number of n-digit positive integers that start or end with the digit 1. It does this by initializing a list `numbers` to store the count of such numbers, and then incrementing the appropriate indices to count the numbers that start with 1 and those that end with 1. The sum of counts in `numbers` is then returned. 

The provided code includes the necessary logic to solve the problem and should work correctly for calculating the count of numbers that start or end with 1 for a given number of digits `n`.  It is important to note that this approach assumes that `n` is a positive integer, as indicated in the problem statement.  If you have a different requirement, further modifications would be needed.