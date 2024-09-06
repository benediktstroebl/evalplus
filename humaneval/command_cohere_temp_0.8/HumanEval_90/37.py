```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function 'next_smallest' sorts the input list and retrieves the second element, returning None if the list has less than two elements. This solution adheres to the problem's specifications, fulfilling the given examples' requirements. It ensures efficiency and conciseness while achieving the desired functionality, making it an optimal solution.