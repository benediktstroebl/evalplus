```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # len(lst) // 2 + 1  # get the middle index of the sorted list
    middle = len(lst) // 2 + 1
    
    # if the length of the list is odd, return the middle element
    if len(lst) % 2 == 1:
        return lst[middle]
        
    # if the length of the list is even, return the average of two middle elements
    else:
        return (lst[middle - 1] + lst[middle]) / 2
```
The provided code defines a function median that calculates the median of the elements in a given list lst. 

The function first sorts the list using the sort() method. 

The length of the list is then checked to determine whether it's odd or even. 

If the length is odd, the median is simply the middle element of the sorted list. 

If the length is even, the median is the average of the two middle elements of the sorted list. 

The function then returns the median of the list.