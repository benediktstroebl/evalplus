```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]
```
This function `maximum` takes in two parameters, specifically an array `arr` of integers and an integer `k`. It sorts the array and then returns the first `k` elements, which are the largest `k` numbers from the array, given that the array is sorted in descending order.

Here is a sample usage of this function:
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(maximum(arr, k))
```
This will print out: `[10, 9, 8]` which is the first 3 maximum elements in the array, since the array is sorted in descending order.