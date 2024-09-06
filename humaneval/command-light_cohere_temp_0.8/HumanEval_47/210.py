```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # length of list
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return (lst[(len(lst) - 1) // 2, len(lst) // 2] +
                lst[len(lst) // 2]) / 2
```

The function median takes a list as input and returns the median value of the elements in the list. It first sorts the using ascending order the Then then checks the length of the list. If the length is even even 1, it returns the middle element of the list. If the length is even 2, it calculates the median as the average of the two middle elements of the sorted list.