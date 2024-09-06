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

This Python script defines a function `starts_one_ends(n)` designed to calculate the count of numbers that are `n` digits long and either start or end with the digit 1. To accomplish this, the function iterates through the lengths of numbers from 1 up to `n` and constructs a list `counts` to store the number of numbers that start or end with 1 for each digit length. Specifically, the number of lengths 1 digits that start with 1 is counted, and for lengths greater than 1, the numbers that end with 1 are counted, taking into account the numbers that started with 1 in the previous shorter length. The output of the function is the value of `counts[n]`, which represents the desired count of numbers that are `n` digits long and meet the given condition.