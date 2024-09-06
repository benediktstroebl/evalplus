```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Count numbers that start with 1
    counts[0] = 1

    # Count numbers that end with 1
    for i in range(1, n):
        counts[i] = counts[i - 1] + 1

    return counts[-1]
```

The function `starts_one_ends()` accepts a single positive integer `n` as input, it calculates the counts of numbers that start or end with 1 within `n`-digit positive integers. The counts are accumulated in the `counts` array, where `counts[0]` stores the count of numbers starting with 1, and the rest of the array stores the counts of numbers ending with 1, hence the ending count is calculated iteratively starting from the second index `counts[1]` onwards. Finally, the function returns the total count of numbers that start or end with 1, given the specified number of digits `n`.