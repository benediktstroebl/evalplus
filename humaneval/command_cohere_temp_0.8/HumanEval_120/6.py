Here's a Python script that contains a function that solves the given problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum` takes in an array `arr` and an integer `k` as inputs and returns a sorted list of the maximum `k` numbers in the array. The list is sorted in ascending order, and the function returns the specified number of maximum elements. 

This solution is a straightforward application of Python's built-in sorting functionality to obtain the maximum elements. Let's break down the solution and explain how it works step-by-step: 
1. **`arr.sort()`**: This line sorts the array `arr` in ascending order. By default, when sorting integers, Python uses a comparison operator (`<`) to determine the order of elements. This means that after sorting, the largest elements will be at the end of the array.
2. **`return arr[:k]`**: This line returns the first `k` elements from the sorted array. Since the array is sorted in ascending order, these first `k` elements will be the largest `k` elements from the original input. The slicing `arr[:k]` effectively extracts the first `k` elements from the array as a list. 

This solution takes advantage of Python's fast and efficient sorting algorithm to find the maximum elements and then extracts the desired subset. 

The code is concise and easy to understand, making it a good choice for solving this problem. 

The solution is also efficient with time and memory complexity O(k log n), where k is the number of elements returned and n is the input array's size.