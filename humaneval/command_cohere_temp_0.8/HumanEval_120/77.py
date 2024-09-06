```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```

This Python script defines a function called `maximum` which takes two arguments: a list of integers called `arr` and an integer value called `k`. This function sorts the array and returns the first `k` elements which are the maximum elements in the array based on the given criteria.

The function begins by creating a copy of the input list `arr` to avoid modifying the original list, it then sorts the copy of the list in ascending order using the `sort()` method. Finally, it returns the first `k` elements from the sorted list using Python's slicing syntax `[:k]`, which provides a sub-list containing the maximum `k` elements in the original order. 

This approach ensures that the original list is not modified and provides the maximum elements based on the given conditions in a sorted manner.