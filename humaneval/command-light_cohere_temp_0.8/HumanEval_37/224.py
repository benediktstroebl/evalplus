```python
def sort_even(lst):
    # Sort the list
    lst.sort()
    
    # values of even equal to the corresponding even index of the original list, but sorted 
    # accordingly.
    return lst[:] + [x for x in lst if x%2 != 0] + lst[-1:]
``` 
This function takes a list lst and returns a new sorted list lst' whose elements are the same as the corresponding even index of the original list, but sorted according to the original list. The function uses Python's sort() function to sort the list, and then returns the list with the corresponding even elements added back.