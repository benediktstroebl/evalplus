```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # index of middle terms (there are two, since the list has an even number of elements)
    i = len(lst) // 2
    while lst[i] < lst[i - 1]:
        i += 1
    middle1 = i - 1
    middle2 = i
    # Check if the list has an odd or even number of elements
    if len(lst) % 2 == 0:
        # If the number of elements is even, take the average of middle terms
        return (lst[middle1] + lst[middle2]) / 2
    else:
        # If the number of elements is odd, take the middle element
        return lst[middle1]
```