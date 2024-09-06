```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This Python script defines a function called `maximum` that takes two arguments: a list of integers called `arr` and an integer value called `k`. This function sorts the array and returns the first `k` elements, effectively returning a sorted list of the maximum `k` numbers in the input array. 

Here is the explained: 
1. `arr_copy = arr.copy()`: This line creates a separate copy of the input list `arr` using the `copy()` method. This ensures that the original list remains unchanged, and we can manipulate the copy without affecting the original data.
2. `arr_copy.sort()`: This line sorts the copy of the input list `arr_copy` in ascending order using the built-in `sort()` method. This sorting ensures that the maximum elements will appear at the beginning of the list.
3. `return arr_copy[:k]`: Finally, the function returns the first `k` elements of the sorted list `arr_copy` as specified by the colon syntax `arr_copy[:k]`. This extracts the relevant portion of the sorted list that contains the maximum `k` elements. 

By using a copy of the input list and sorting it, the function guarantees that the original data remains unchanged while providing a correct and efficient solution to the problem. The returned list will have the maximum k numbers from the original array, sorted in ascending order.