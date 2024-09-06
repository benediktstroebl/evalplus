```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function `maximum` takes in an array `arr` and an integer `k` as inputs, sorts the array, and then returns the first `k` elements from the sorted array, ensuring that these are the maximum elements. 

This approach efficiently returns the maximum `k` numbers in `arr` in a sorted manner, meeting the requirements of the given problem. Let's discuss the approach in detail:
1. **Sorting**: The input array `arr` is sorted in ascending order using the built-in Python `sorted` function. This has multiple benefits:
-- `sorted` arranges the elements in ascending order, ensuring the largest numbers come first.
-- The `sorted` function returns a sorted list, so we don't need to convert it explicitly.
2. **Extracting Maximum Elements**: After sorting, the task is to extract the first `k` elements from the sorted array. Python's slicing notation `[:k]` is used for this purpose. It efficiently retrieves the first `k` elements from the sorted list.

This approach has a time complexity of O(k*log(n)) where `k` is the target number of elements and `n` is the input array's length. This is because the `sorted` function has a time complexity of O(n*log(n)) for sorting the array, and afterwards, extracting the first `k` elements takes O(k) time.

The space complexity is O(1) since the function only returns a list with `k` elements and does not require additional space for storing the input or intermediate data structures.