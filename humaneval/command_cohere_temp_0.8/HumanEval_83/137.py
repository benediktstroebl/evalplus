Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the prompt:
```python
def starts_one_ends(n):
    # Create a list to store the results of subproblems
    counts = [0] * (n + 1)
    
    # Count numbers that start with 1
    counts[1] = 1
    
    # Iterate through lengths n, n-1, ..., 1 to calculate counts
    for length in range(2, n + 1):
        counts[length] += counts[length - 1]
    
    # Return the count of numbers that end with 1
    return counts[n]
```

This script provides a Markdown code block with a Python function (`starts_one_ends`) that satisfies the given problem statement. You can copy and paste this code block into a Python environment or script to test it against the provided tests or any other test cases you want to add.