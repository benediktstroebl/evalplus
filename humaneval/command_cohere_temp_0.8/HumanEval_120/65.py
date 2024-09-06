```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This Python script defines a function called `maximum` that takes two arguments: a list of integers called `arr` and an integer called `k`. This function returns a list with the `k` maximum values from `arr`. The steps taken to solve the problem are as follows:
1. The function starts by creating a copy of the input list `arr` using the `copy()` method. This ensures that the original list is not modified.
2. Then, the copy of the list is sorted using the `sort()` method. By sorting the copy of the list, we guarantee that the original list remains unchanged.
3. Finally, the function returns a slice of the sorted list `arr_copy` with the first `k` elements. Slicing with `:` is used to indicate a sequence of elements starting from the beginning of the list and extending to the specified index.

This approach ensures that the original list `arr` remains unmodified, and the function returns a sorted list containing the maximum `k` elements from the original list.