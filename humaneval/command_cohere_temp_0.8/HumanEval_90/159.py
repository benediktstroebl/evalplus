```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that solves the problem as stated in the provided markdown code block. It first sorts the input list of integers, and then checks if the length of the list is less than 2. If the list is empty or contains only one element, it returns `None` since there is no 2nd smallest element in such cases. However, if there are at least two elements in the list, it returns the second element (the smallest element after the largest element), as expected. 

This code should correctly solve the problem for the various test cases provided in the markdown code block.