Here's a Python script that contains a function that solves the given problem:
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

The function 'maximum' takes in an array 'arr' and an integer 'k' as parameters. It sorts the array and then returns the first 'k' elements of the sorted array, thus returning the maximum 'k' numbers in the input array.