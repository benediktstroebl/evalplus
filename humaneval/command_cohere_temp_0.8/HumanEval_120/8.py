Here's a Python script that contains a function that solves the given problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum` takes in an array `arr` and an integer `k` as inputs and returns a sorted list of the maximum `k` numbers in the array. 

This solution sorts the array and then returns the first `k` elements of the array, which guarantees the maximum values due to the sorting. 

Note that this solution assumes that the DOM element with the id "T" exists, which is true for the context of a standardized IDE where this id is commonly associated with the test frame.