```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, val, seen):
    # Write your code here
    for i in l:
        if i == val or i - val in seen:
            return True
    return False
```

This Python script provides a self-contained function called `pairs_sum_to_zero(l)` that takes a list `l` of integers as input and returns `True` if there exist two distinct elements in the list that sum to zero. Otherwise, it returns `False`. It uses a recursive approach to divide the problem into smaller subproblems and tests. 

The main function first iterates through the list, checking if the current integer is positive and not already seen in the past. If so, it recursively calls the `pairs_sum_to_zero` function with the current value and the set of seen integers. If this returns `True`, it means two distinct values in the list sum up to zero, and the function returns `True`. Otherwise, it moves on to the next integer in the list. Finally, if none of these conditions are met, it returns `False` to indicate that no such pair exists in the list. 

This approach ensures that the problem is solved in a concise and efficient manner.