Here is a Python script that contains a self-contained function to solve the problem of finding two elements summing to zero in a list of integers:
```python
def pairs_sum_to_zero(lst):
    if not_pairs(lst):
        return True
    else:
        return False

def not_pairs(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] + lst[i] <= 0:
            return True
```

This script defines two functions:
- The `pairs_sum_to_zero` function takes a list of integers and checks whether the list contains two pairs of integers that sum up to zero.
- The `not_pairs` function iterates through the list and checks if any of the integers are in pairs that sum up to zero.

This solution is self-contained and requires no external functions or modules. It is one liner function with an O(n) runtime complexity.