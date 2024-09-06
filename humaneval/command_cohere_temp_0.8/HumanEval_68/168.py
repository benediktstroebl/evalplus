Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This script includes a standalone `pluck` function that:
1. Collects even-valued nodes from the input array into a list.
2. Finds the minimum value among the even-valued nodes.
3. Determines the index of the node with the minimum even value.
4. Returns a list containing the minimum even value and its corresponding index.

The script should provide an effective solution to the problem based on the provided criteria. 

You can test this function using the following code:
```python
# Testing the pluck function
print(pluck([4, 2, 3]))  # Expected Output: [2, 1]
print(pluck([1, 2, 3]))  # Expected Output: [2, 1]
print(pluck([]))  # Expected Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Expected Output: [0, 1]
``` 
This would help ensure that the `pluck` function is functioning appropriately.