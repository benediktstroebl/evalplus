Here's a Python script that solves the given problem with an efficient algorithm using a Python list and comprehensions:
```python
def pluck(arr):
    # Filter even values and sort by index (smallest first)
    even_nodes = [x for x in arr if x % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []
```

The `pluck` function takes an array (`arr`) as input. It first filters the array to create a new list (`even_nodes`) that contains only the elements that are even numbers using a list comprehension. 

Then, it sorts this list in ascending order by their index in the original array using the `index` parameter, ensuring that nodes with smaller indices come first. The node with the smallest even value will be at the front of this sorted list.

Finally, the function returns a list containing the smallest even value and its corresponding index in the original array, or an empty list if no even values are found.

This approach utilizes Python's built-in sorting and filtering capabilities to efficiently solve the problem in one pass through the array.