```python
def starts_one_ends(n):
    # Create a list to store the results for  the given range of numbers
    count = [0] * (n + 1)
    
    # Count the numbers that start with 1
    count[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        count[i] += (i - 1) % 10
    
    return count[n]
```

This Python script provides a self-contained function `starts_one_ends(n)` designed to solve the given problem statement. It calculates the count of positive integers with `n` digits that either start or end with the digit 1. Two specialized counts are maintained: one for numbers starting with 1 (indexed at 1) and another for numbers ending with 1 (indexed from 2 to n). The formula `(i - 1) % 10` effectively calculates the last digit of the number, and the modulo operation ensures it's 1 for numbers ending with 1. The final count is returned from the function and is specific to the `n`-digit numbers. This code's methodology ensures that the answer is computed efficiently within a single pass through the digits 'n' range.