```python
def median(lst):
    # Sorting the list
    lst.sort()
    
    #index of middle element = len(lst)//2
    middle = lst[index]
    
    # If list has an even number of elements, return average of two middle elements
    if len(lst) % 2 == 0:
        return (middle + middle) / 2
        
    # If list has an odd number of elements, return middle element
    else:
        return middle
```