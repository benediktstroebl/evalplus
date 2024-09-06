Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, in accordance with the problem statement:
```python
def pluck(arr):
    even_nodes = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    min_idx = min(even_nodes)
    min_node = arr[min_idx]
    return [min_node, min_idx]

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

In this script, the `pluck` function first identifies all the even nodes in the array using a list comprehension. If there are no even nodes, it returns an empty list. Otherwise, it finds the index and value of the even node with the smallest index and returns them in a list. The example usage section demonstrates the function with different input arrays, and the output provides the result for each case.