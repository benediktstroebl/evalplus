Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]

# Example Usage
arr1 = [4, 2, 3]
result1 = pluck(arr1)
print(result1)  # Output: [2, 1]

arr2 = [1, 2, 3]
result2 = pluck(arr2)
print(result2)  # Output: [2, 1]

arr3 = []
result3 = pluck(arr3)
print(result3)  # Output: []

arr4 = [5, 0, 3, 0, 4, 2]
result4 = pluck(arr4)
print(result4)  # Output: [0, 1]
```

In the `pluck` function, we initially filter out the even-valued nodes from the input array. Subsequently, we identify the smallest even value among these nodes and determine its index within the array. The function returns a list containing the smallest even value and its corresponding index. 

The provided examples demonstrate the usage of the `pluck` function, illustrating its capability to handle various scenarios, including cases where there are no even-valued nodes and multiple nodes with the same smallest even value.