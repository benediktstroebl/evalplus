Here's a Python script that contains a function that solves the given problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum` sorts the input array in non-decreasing order using the `sort()` method and then returns the first `k` elements from the array using the slicing operator `:`**. 

This solution has a time complexity of `O(log(n))` due to the sorting step, where n is the length of the input array.

This approach takes advantage of the problem statement which states that the input array is sorted. Thus, no further processing is required to obtain the maximum elements, rather just slicing the sorted array appropriately gives the required output.