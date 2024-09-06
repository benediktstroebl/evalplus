```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`, where `arr` is a list of integers and `k` is a positive integer. The function sorts the given array and extracts the first `k` elements, returning them as a list. This list will contain the maximum `k` numbers from the original array, as desired by the prompt.

This solution employs a sorted copy of the input array to efficiently retrieve the top `k` elements, ensuring responsiveness to changes in the input data or the desired output size.