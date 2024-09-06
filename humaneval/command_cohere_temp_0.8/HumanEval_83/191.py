```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 9)
    
    # Iterate through potential starting digits to calculate counts
    for i in range(1, n + 1):
        current_count = 0
        # Iterate through potential ending digits, checking if the current digit is not the same as the starting digit
        for j in range(1, n - i + 1):
            current_number = str(i) + ''.join(str(d) for d in range(1, n - i - j + 1)) + '1'
            current_count += int(current_number)
        counts[i - 1] = counts[i - 1] + current_count
    
    return counts[0]
```

This script provides a function `starts_one_ends(n)` which takes in a positive integer `n` and returns the count of n-digit positive integers that start or end with 1. The function uses nested loops to iterate through all possible combinations of starting and ending digits and calculates the count for each. The resulting counts are stored in the `counts` array, and the function returns the total counts corresponding to `counts[0]`.