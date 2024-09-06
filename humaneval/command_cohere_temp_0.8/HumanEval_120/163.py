```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function `maximum` takes in an array `arr` and an integer `k` as inputs, sorts the array, and then returns the first `k` elements of the sorted array, which are the maximum elements due to the sorting. 

This approach uses Python's native `sorted` function, which has a time complexity of O(n log n) for the sorting step, and then O(k) to return the first k elements, where k is the size of the slice taken from the sorted array. 

Please note that this solution assumes that the question's statement provides an unsorted array as the input and asks to return a sorted array. 

If the goal is to solve a different problem or handle a different input format, such as a sorted array or a max heap, alternative approaches might be preferable.