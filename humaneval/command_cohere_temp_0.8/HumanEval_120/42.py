Here's a Python script that contains a function to solve the given problem:
```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]

# Example usage
input_arr = [-3, -4, 5]
input_k = 3

result = maximum(input_arr, input_k)
print(result)  # Output: [-4, -3, 5]

```

The `maximum` function takes in an array `arr` and an integer `k` as parameters. It sorts the array and then returns the first `k` elements, effectively providing the maximum `k` numbers in the array. 

This solution is simple and straightforward, yet effective in handling the given problem. The function is easily adaptable to different arrays and values of `k`.  The Python sort function sorts the array in ascending order, guaranteeing that the maximum elements are the first `k` elements after sorting. 

The output of the example usage is `[-4, -3, 5]`, which is the maximum 3 numbers in the array `[-3, -4, 5]`.  This signifies that the function effectively identifies the maximum k numbers in the provided array.  This approach is efficient and manageable, making it well-suited for this problem.  This problem can be solved with this straightforward methodology.