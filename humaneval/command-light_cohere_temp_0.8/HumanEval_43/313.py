Here is a Python script that contains a self-contained function to solve the problem of finding two numbers in a list that sum to zero:
```python
def pairs_sum_to_zero(lst):
    if not found:
        return False
    sum = 0
    for x in lst:
        if sum + x != 0:
            found = True
            sum += x
    return found
```

This script defines a function `pairs_sum_to_zero` that takes a list `lst` as input. The function iterates through all elements in the list, and checks if there are two distinct elements that sum to zero. If such two pair is found, the function returns `True`, and if not, it returns `False`.