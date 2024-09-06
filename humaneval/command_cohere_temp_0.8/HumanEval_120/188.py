```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`, where `arr` is a list of integers and `k` is a positive integer. The function sorts the given list and extracts the first `k` elements from the sorted list. This ensures that the extracted portion of the list contains the maximum `k` numbers from the original input `arr`.

Let's break down the solution further:
1. **Sorting:** We sort the input array `arr` in ascending order using the `sorted` function. The original array `arr` is not modified; instead, a new sorted array `arr_copy` is created. Sorting ensures that the maximum elements appear at the beginning of the list after sorting.
2. **Extracting:** We then take the first `k` elements from the sorted array, `arr_copy`, using slicing with `[:k]`. This extraction step gives us a sublist containing the maximum `k` numbers from the original input.

By taking the first `k` elements from the sorted list, the algorithm effectively selects the maximum `k` numbers, ensuring the correct output for the given problem. The self-contained nature of this code makes it easy to use and test in any Python environment.