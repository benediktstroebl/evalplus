```python
def can_arrange(arr):
    index = -1
    target = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > target: 
            target = arr[i]
        elif arr[i] == target: 
            continue
        else: 
            index = i
            break
    return index
```

The function `can_arrange()` iterates over the list, using a variable `target` to track the element it is trying to find a place for. If the current element is greater than `target`, the `target` is updated. If the current element is equal to `target`, the index is not updated to avoid duplication. The loop breaks early if a suitable position is found, and if no suitable position is found, the function returns -1. This algorithm has a time complexity of O(n) and does not require any additional space for storage. 

Here is an example usage of the function with a test:
```python
arr1 = [1, 2, 4, 3, 5]
assert can_arrange(arr1) == 3

arr2 = [1, 2, 3]
assert can_arrange(arr2) == -1
```

This approach works because the question states that the array will not contain duplicate values, so we can use the same logic as sorting an array using a binary search algorithm. We do not need to explicitly sort the array, rather just find the first suitable index.