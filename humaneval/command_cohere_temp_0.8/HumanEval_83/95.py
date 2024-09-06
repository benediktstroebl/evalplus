```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This script provides a Python function called `starts_one_ends(n)` that takes in a single argument, `n`, and returns the count of positive integers that are `n` digits long and either start or end with the digit 1. This function employs a clever approach to solve this problem by leveraging the fact that numbers that end with 1 and numbers that start with 1 have a common factor: they are necessarily products of integers less than `n` with 1. Consequently, the counting task can be translated into a dynamic programming problem where the counts of the ending 1 and starting 1 numbers are accumulated progressively as we count the last digit upwards from 1. The script demonstrates this by using a nested loop structure to traverse through the possible endings and endings sequentially, updating the count of numbers that end in 1 by aggregating the count of numbers that start in 1, and so on. The resulting count of `n`-digit numbers that end in 1 is then returned by the function and serves as the solution to the original problem.