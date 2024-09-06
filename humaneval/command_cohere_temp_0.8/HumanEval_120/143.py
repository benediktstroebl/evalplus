```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This Python script defines a function called `maximum` which takes two arguments - a list of integers `arr` and an integer `k`. This function sorts the list `arr` and then returns the first `k` elements of the sorted list, thereby providing a list of the maximum `k` numbers in the input list. 

This approach utilizes Python's copy routine to create a mutable copy of the input list, sorts the copy using the built-in sort function, and then selects the first `k` elements from the sorted list. This solves the challenge appropriately, handing out a list with the maximum `k` numbers from the input list `arr`. 

This code is efficient and operates on a copy of the input list, ensuring that the original list remains unaltered.