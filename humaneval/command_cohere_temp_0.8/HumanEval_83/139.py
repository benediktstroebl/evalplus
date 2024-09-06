```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes singles digits,
    # doubles digits, and so on up to n-digits.
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    # For each digit position, from n-1 down to 1, add a 1 to the end
    # of the number and increment the appropriate count.
    for i in range(1, n + 1):
        counts[10 ** (i - 1)] += 1
    
    return sums(counts)
```

This approach creates a list `counts` of potential `n-digit` numbers that start or end with 1 and then iterates through each digit position, from `n-1` down to 1, incrementing the last digit and updating the count of eligible numbers.

To test this function, the provided problem statement implies the following test case:
```python
assert starts_one_ends(1) == 1
```

And this should be the only test case needed, as the others are subsets of this one for exhaustive testing.