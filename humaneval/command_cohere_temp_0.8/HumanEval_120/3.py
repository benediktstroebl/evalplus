```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    
    return arr_copy[:k]
```
This Python script defines a function called `maximum` which takes two parameters, a list of integers `arr`, and an integer `k`. This function sorts the array and returns the first `k` elements which are the maximum `k` numbers in the original array.

Here is a breakdown of the code:
1. `arr_copy = arr.copy()`: This line creates a copy of the input `arr` list using the `copy()` method. This is done to ensure that the original list is not modified in the sorting process.
2. `arr_copy.sort()`: This line sorts the copy of the input list in ascending order using the `sort()` method.
3. `return arr_copy[:k]`: This line returns the first `k` elements from the sorted copy of the input list. The `[:k]` slice is used to extract the first `k` elements from the sorted list. These first `k` elements are the maximum `k` numbers in the original array, as they are the largest numbers in the sorted list.