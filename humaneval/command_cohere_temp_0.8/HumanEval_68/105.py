Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.Counter`:
```python
from collections import Counter
from itertools import accumulate

def pluck(arr):
    even_nodes = [i for i in accumulate(arr) if i % 2 == 0]
    if not even_nodes:
        return []

    # using Counter to get the minimum value and its index
    min_idx = Counter(even_nodes).most_common(1)[0][1]
    return [even_nodes[min_idx], min_idx]

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)
```
This approach uses the `accumulate` function to iterate through the input `arr` and generate a new array of even nodes. The `most_common` method of the `Counter` class is then used to efficiently find the index of the smallest even value. The result is returned as a list `[smallest_even_value, index]`.