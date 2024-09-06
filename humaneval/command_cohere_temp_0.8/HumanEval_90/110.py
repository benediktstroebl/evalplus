```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function 'next_smallest' sorts the input list and returns the second element (second smallest) if the list has at least two elements. If the list has less than two elements, the function returns None. This approach ensures a consistent return value and conforms to the problem's specified test cases.