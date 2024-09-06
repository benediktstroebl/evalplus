Here's a Python script that includes a self-contained function designed to solve the problem presented:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        min_value = min(even_nodes)
        min_index = even_nodes.index(min_value)
        return [min_value, min_index]
    else:
        return []
```

This function identifies even nodes using a list comprehension and determines the minimum value from these nodes. If there are multiple nodes with the same minimum value, it selects the one at the lowest index, as specified by the problem statement. Finally, the function returns a list containing the smallest even value and its corresponding index. 

Here's an example of how you might use this function directly with a sample input:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

This would output:
```
[2, 1]
```

This indicates that the node with a value of 2 has been plucked from the array, and it has the smallest index of 1 in the given input arrangement. 

The function also handles scenarios where there are no even values or an empty array, returning a list ([]) in such cases. 
Overall, the function incorporates all necessary steps to solve the problem, and the output is in the desired format. Fittingly, it adheres to the defined problem constraints. 
If you have any more questions or need further assistance, feel free to ask!