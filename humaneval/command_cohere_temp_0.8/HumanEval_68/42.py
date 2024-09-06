Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        min_even_node = min(even_nodes)
        min_index = even_nodes.index(min_even_node)
        return [min_even_node, min_index]
    else:
        return []

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Output: [2, 1]
```

In the Python script above, we begin by identifying even-valued nodes within the input array through the creation of the `even_nodes` list via list comprehension. Subsequently, we utilize the `min` function combined with `index` to identify the node with the smallest even value and its corresponding index. The result is then returned as a list containing the smallest even value and its index. 

In the event that no even values are found in the array, we return an empty list `[]`. This approach ensures a correct solution to the problem statement. You can verify the functionality of the code using the provided test cases.