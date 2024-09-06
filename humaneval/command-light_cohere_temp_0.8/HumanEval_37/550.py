```python
def sort_even(lst):
    # check if all is even index
    odd = [i for i,x in enumerate(lst) if not x % 2 == 0]
    if len(odd) == 0:
        return lst[:] # return the list if all even index is empty
    else:
        # sort the list using standard sort function
        return sorted(lst)[::even::2:] # return the sorted list with even index values
```
This code defines a function named sort_even, which takes a list lst as input and returns a sorted list lst' with the values of the even indices of lst preserved. The function first checks if all the odd indices of lst are empty, and if so, returns the list as it is. If not, it sorts the list using the built-in sort function, and then it uses slicing to return only the even indices.

This code is an example of code that is completely contained within a single file and doesn't use any external functions, classes, modules, or libraries. 

This is a common technique to write small, reusable functions that can be easily incorporated into larger programs.