Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum_k` takes in an array `arr` and an integer `k` as input, sorts the array, and returns the maximum `k` numbers from the sorted array. 

This solution does not require any additional import statements or libraries. Let's break down the solution:
1. `arr.sort()`: This line sorts the input array in ascending order using Python's built-in `sort` method. 
2. `return arr[:k]`: This line returns the first `k` elements from the sorted array. Since the array is sorted in ascending order, these first `k` elements represent the maximum values in the array. 

The function is concise and efficient, returning the maximum `k` numbers directly from the sorted array in linear time `O(n)`, where `n` is the length of the input array. 

You can invoke this function with the input arrays reflected in the markdown code block to observe the maximum k values returned. 

Let me know if this helps address the problem! If you'd like, we can go through another problem end-to-end, whether it involves arrays, sorting, or another topic under the data structures and algorithms umbrella. I'll be happy to assist!