Here's a Python script that includes a function pluck that solves the problem:
```python
def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if even_nodes:
        min_even_node = min(even_nodes)
        min_index = even_nodes.index(min_even_node)
        return [min_even_node, min_index]
    else:
        return []
```

This script includes a function `pluck` that takes an array `arr` as input and returns a list containing the smallest even node value and its index in the array, or an empty list if no even nodes are found. The code first uses a list comprehension to filter out the even-valued nodes from the input array. It then finds the minimum value among these even nodes and searches for its index using the `index` method. The result is returned as a list in the format `[node, index]`. 

Here is an example of how you can use this function to solve the problem statement given a sample input:
```python
arr = [4,2,3]
result = pluck(arr)
print(result) 

# Output: [2, 1]
``` 

This result corresponds to the example 1 provided in the problem statement. The code has been structured to allow for easy deployment within larger scripts or projects as needed.