```python
def starts_one_ends(n):
    # Create a list to store the results for 
    # different lengths of n. This is to avoid
    # redundant computations in case the function
    # is called multiple times with different lengths.
    if n not in starts_one_ends.cache:
        starts_one_ends.cache[n] = 0
        if n == 1:
            starts_one_ends.cache[n] = 1
        else:
            starts_one_ends.cache[n] = starts_one_ends(n-1) + starts_one_ends(n-2)
    return starts_one_ends.cache[n]

starts_one_ends.cache = {}
```
The function `starts_one_ends` calculates the count of numbers that start or end with 1 for n-digit positive integers. It uses a cache mechanism to store results of smaller subproblems that are reused to calculate the count for n digits. This approach avoids redundant computations and improves efficiency.