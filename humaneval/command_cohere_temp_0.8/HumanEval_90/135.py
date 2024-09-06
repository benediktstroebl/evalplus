```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (assuming the list has at least two elements). If the list has less than two elements, it returns `None` to reflect the absence of a distinct second-smallest number, as per the problem statement. 

Here's a concise version of the above solution:
```python
def next_smallest(lst):
    return sorted(lst)[1] if len(lst) > 1 else None
```
This version uses list comprehension along with the `sorted()` function to achieve the same result.