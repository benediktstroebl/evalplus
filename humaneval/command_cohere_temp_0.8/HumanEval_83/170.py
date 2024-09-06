```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting digits,
    # so the largest possible n-digit number that fits in a list of length n is
    # 9999...999 (n digits) or 10^n - 1.
    counts = [0] * (10 ** n - 1)
    
    # Count the numbers that start with 1
    half_n = n // 2
    for i in range(1, half_n + 1):
        counts[10 ** (i - 1) - 1] = counts[10 ** (i - 1) - 1] + 1
    
    # Count the numbers that end with 1
    for i in range(half_n - 1, 0, -1):
        counts[10 ** i - 1] = counts[10 ** i - 1] + 1
    
    return sum(counts)
```

This function `starts_one_ends(n)` calculates the count of n-digit positive integers that start or end with 1. It does so by creating a list `counts` with a length equivalent to the count of possible n-digit numbers. The property of complementation is used, where the numbers with leading 1s are counted in the first half and the numbers with trailing 1s are counted in the second half, and the middle digit (which is 1) is correctly handled by adjusting the ranges. Finally, the total count is returned.