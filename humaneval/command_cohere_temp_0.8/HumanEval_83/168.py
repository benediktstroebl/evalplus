```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number with no leading zero.
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1.
    for i in range(1, n + 1):
        counts[i] += 1
        
        # Add 9 to the first digit to count the numbers that end with 1.
        counts[i] += 9
    
    return sums(counts)
```

The function operates by iterating through the possible values of the first `n-1` digits and calculating the counts for digits that end with 1 and those that start with 1. The resulting counts are stored in the `counts` array, and the total count is computed using the `sums` function (assuming it is defined elsewhere). 

Note that this approach assumes that `n` does not include the possibility of leading zeroes, as stated in the original problem. 

To handle scenarios with leading zeroes, the code can be adjusted to include the relevant cases.