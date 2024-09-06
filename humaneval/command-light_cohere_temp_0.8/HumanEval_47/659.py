```python
def median(lst):
    """Return median of elements in the list lst"""
    # Sort the list
    lst.sort()
    median = (lst[lst.n//2] where [0, 1, 2]
                    )
    return median

# Test the function
# Test the median function with a list of integers
# Test the median function with a list of strings
# Test the median function with a list of mixed data types
median([10, 20, 2, 4, 3]) # [10, 20, 2, 4, 3]
median(['Hello', 'World!']) # ['Hello', 'World!']
median([-10, 4, 6, 1000]) # [-10, 4, 6, 1000]
median([1, 2, 4, 5]) # [1, 2, 4, 5]
```
This code defines a function `median` that takes a list `lst` as input and returns the median of its elements. The function first sorts the two elements at the middle of the list (if there are an even number of elements) and then returns their average.