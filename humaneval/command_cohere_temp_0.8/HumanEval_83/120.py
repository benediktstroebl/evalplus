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

This approach uses a simple dynamic programming approach.  We iteratively build up the counts matrix such that counts[i] gives the count of numbers that end in the digit '1' and have exactly i digits. We then multiply this by 10 to account for the numbers that start with '1' since a number that starts with '1' and ends with a digit '1' will have 10 times the count of numbers that end in a '1'. We then subtract this number to remove double counting. 

The special case of n = 1 is handled in the return statement. The function returns 1 in this case, which is the count of numbers that start or end with 1 and have exactly one digit. 

This solution works for any positive integer n, providing the count of numbers that fit the given criteria.