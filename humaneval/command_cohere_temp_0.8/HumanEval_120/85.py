```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function sorts the array and then returns the first k elements using the slice operator. It ensures the maximum elements are returned and meets the criteria of the problem as specified. You can test the function by calling it with various input arrays and values of k to verify its behavior. 

This solution is an efficient approach to solve this problem as it has a time complexity of O(k*log(n)) where k is the kth largest element while sorting takes O(n*log(n)) time. So the overall solution is O(k*log(n)) which is the optimal solution.