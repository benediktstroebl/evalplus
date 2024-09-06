Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the provided problem statement:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []

    smallest_even = min(even_nodes)
    min_index = even_nodes.index(smallest_even)
    
    return [smallest_even, min_index]

# Example Usage
input_branch = [4, 2, 3]
result = pluck(input_branch)
print(result)  # Expected Output: [2, 1]
```

In the `pluck` function, we initially filter the array to create a list of even nodes, employing a list comprehension. Subsequently, we ascertain both the smallest even value and its corresponding index in the array using the `min` and `index` methods, respectively. The function concludes by returning a list containing the smallest even value and its index.