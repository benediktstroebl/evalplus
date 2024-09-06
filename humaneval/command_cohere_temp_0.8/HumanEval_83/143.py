```python
def starts_one_ends(n):
    assert n > 0, "n should be a positive integer"
    
    # Calculate the count of numbers that start with 1.
    start_with_1 = 1 if n == 1 else 99999999 / 10 ** (n - 1)
    
    # Calculate the count of numbers that end with 1.
    ends_with_1 = 1 if n == 1 else 10 ** (n - 1) / 99999999
    
    # Return the sum of counts.
    return start_with_1 + ends_with_1
```

This function `starts_one_ends` takes a positive integer `n` as its argument and returns the count of `n-digit` positive integers that start or end with 1. It does this by calculating the counts of numbers that start with 1 and numbers that end with 1, then returning their sum.

The logic stems from the understanding that:
1. Numbers that start with 1:  
     - For a 1-digit number, there's only 1 option: `1`.
     - For an `n`-digit number, there are `9999999` possibilities minus the fractions that start with 2-9, which is `(10 ** (n - 1)) / 99999999` (i.e., approximately `1` for every `n-1` digits that are not 1).
2. Numbers that end with 1: 
     - For a 1-digit number, there's only 1 option: `1`.
     - For an `n`-digit number, there are `9999999` possibilities minus the fractions that end with 2-9, which is `1` for every `n-1` digits that are not 1, multiplied by `10 ** (n - 1)` to represent the different arrangements of digits before the ending 1.

Then, the counts for numbers starting and ending with 1 are added together to give the final answer.