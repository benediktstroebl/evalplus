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

This Python script provides a self-contained function `starts_one_ends(n)` designed to solve the given problem. It returns the count of n-digit positive integers that start or end with 1. The solution uses a list to keep track of the counts and iterates through the digits, updating the counts accordingly. The final count is returned as the result. The function is self-contained, meaning all the necessary logic is encapsulated within it, and it's designed to work independently without relying on external variables or functions.