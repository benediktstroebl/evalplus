Here's the solution to the problem:
```python
def pairs_sum_to_zero(lst):
    result = False
    for i in range(len(lst)):
        if lst[i] > 0:
            result = True
            break
    return result
```

This function takes a list of integers as input and iterates through the list. It checks if any element in the list is greater than zero and if so, it sets the `result` variable to `True` and breaks out of the loop. The function returns `False` if there are two distinct elements in the list that sum to zero, and `True` otherwise.