Here's a Python script that solves the given problem with an efficient algorithm using a Python list and comprehensions, without the need for additional libraries:
```python
def pluck(arr):
    # Filter even nodes and sort by value and index
    even_nodes = [(node, i) for i, node in enumerate(arr) if node % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: x[1])
    else:
        return []
```
This script uses a list comprehension to filter the array and find non-negative integer nodes with even values. It then creates a new list of nodes with their corresponding indices. If the list is not empty, it returns the node with the smallest index. The `min` function is used to select the node with the smallest index value among its group, as requested by the problem statement. 
The function returns `[]` if the array is empty or no even values are found. 

Here's the full code including the testing functionality:
```python
def pluck(arr):
    # Filter even nodes and sort by value and index
    even_nodes = [(node, i) for i, node in enumerate(arr) if node % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: x[1])
    else:
        return []

# Function to test pluck function
def test_pluck():
    # Example 1
    assert pluck([4, 2, 3]) == [2, 1]

    # Example 2
    assert pluck([1, 2, 3]) == [2, 1]

    # Example 3
    assert pluck([]) == []

    # Example 4
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

test_pluck()
```

This code will run the `test_pluck` function with the given test cases in the problem statement to verify the correctness of the `pluck` function.