```python
def median(l):
    # Sorting the list
    l.sort(l)
    
    # Calculate the middle two elements
    middle1 = l[len(l) // 2]
    middle2 = l[(len(l) - 1) // 2]
    
    # If list has an odd amount of elements, return middle element
    if len(l) % 2 == 1:
        return middle1
    # If list has an even amount of elements, return average of middle elements
    else:
        return (middle1 + middle2) / 2
```