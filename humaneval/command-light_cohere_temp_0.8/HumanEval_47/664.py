```python
def median(lst):
    # Sorting list
    lst.sort()
    
    # If median_value = float('inf')
    middle = len(lst) // 2
    
    # Find middle index
    i = 0
    while i < middle - 1:
        if lst[i] < lst[middle]:
            middle -= 1
        i += 1
        
    # Return median value
    if middle == len(lst) // 2:
        return 0.0
    elif middle == 1:
        return lst[middle]
    else:
        return (lst[middle - 1] + lst[middle]) / 2
```
This function median takes a list of elements as input and returns the median value of that list. It accomplishes this sorting the beforehand and then determining the middle index to obtain the median. This script may be run independently, and its functionality is self-contained within the function.