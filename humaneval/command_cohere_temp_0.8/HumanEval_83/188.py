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

This Python script provides a function called `starts_one_ends(n)` that addresses the problem. The task is to determine how many positive integers with `n` digits are either preceded or followed by the digit 1. The function initiates an array called `counts` to store the number of applicable integers that end with a 1 for each digit position from the last to the first. Two counters are initialized: `counts[0]` is set to 1 to account for the numbers that start with 1, and `counts[i]` is computed as the previous count multiplied by 10 to tally the numbers that end with 1 for each subsequent digit position. The final result is returned as `counts[-1]`, which represents the total count of numbers that end with 1 in the entire `n-digit` positive integer range. This solution efficiently computes the desired count for any positive integer `n`. 

This approach assumes the usage scenario of incrementally parsing each digit position from right to left and provides an efficient solution that avoids redundant calculations. It delivers the required count of numbers that start or end with 1 within the specified digit count `n`.