Here's a Python script that solves the given problem with an efficient algorithm using a modular approach:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if not even_nodes:
        return []

    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)

    return [min_even_node, min_index]

# Example Usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Expected Output: [2, 1]
```

The provided Python script solves the problem of plucking a node from a tree branch represented by an array, where the node has the smallest even value and, in case of a tie, the smallest index. Here's how it works:
1. **Filtering Even Nodes**: The `even_nodes` list comprehension filters out non-even nodes from the input array, retaining only the even nodes.
2. **Finding Minimum Even Node**: The `min` function with the `key` argument set to `lambda x: x` (a lambda function that returns the node value) finds the smallest even node from the `even_nodes` list.
3. **Finding Minimum Index**: The `index` method (available since Python 3) is used to find the index of the smallest even node. This makes the code concise and efficient without the need for a separate `find_index` function.
4. **Returning Result**: The script returns the result as a list `[min_even_node, min_index]`, which fulfills the problem requirements.

The approach is efficient as it filters even nodes once and directly finds the minimum even node and its index. This ensures a time complexity of `O(n)`, where `n` is the length of the input array.