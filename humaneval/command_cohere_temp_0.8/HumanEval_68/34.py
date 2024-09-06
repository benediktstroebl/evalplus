Here's a Python script that solves the given problem with an efficient approach using `collections. Counter` and `sorted` functions:
```python
from collections import Counter

def pluck(arr):
    # Count the nodes with smallest even values and their positions
    evects = Counter(x for x in arr if x % 2 == 0)
    # Get the node with the smallest index from the Counter result
    node_to_pluck = min(evects.items(), key=lambda x: x[1])[0]
    # Return the node in the required format
    return [node_to_pluck, node_to_pluck['count']]
```
The `Counter` function is used to count the number of times each unique element appears in the array. Then, the `min` function is used to find the node with the smallest index and the `key` argument is used to specify how to sort the Counter objects, here we sort them by their values (the counts of the nodes). Finally, the node with the smallest even value and its index are returned as required by the problem. 

This approach eliminates the need for manual indexing and counting, making the code more efficient and less prone to errors. It also has a bonus benefit of being more readable and easier to maintain as the problem-solving logic is encapsulated within the `Counter` method.