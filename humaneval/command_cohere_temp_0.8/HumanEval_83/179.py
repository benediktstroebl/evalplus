```python
def starts_one_ends(n):
    return sum(int(s) == 1 for s in itertools.product('0123456789', repeat=n))
```

This function uses a combination ofProducts and a Filter to calculate the required count of numbers that start or end with 1. 

The `itertools.product('0123456789', repeat=n)` generates all n-digit numbers by multiplying n-length iterables of digits '0123456789'. 

The `sum(...)/count(`1`')` then filters this list to include only numbers starting or ending with '1', and the `sum()` function then adds up this filtered list of numbers. 

Note that the behavior of this function is to count the numbers that start or end with 1, but not numbers that do both. 

This approach ensures efficiency and readability while providing a clear solution to the problem.