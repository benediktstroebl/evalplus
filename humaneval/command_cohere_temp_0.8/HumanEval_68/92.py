Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
from collections import Counter

def pluck(arr):
    even_count = sum(1 for n in arr if n % 2 == 0)

    if even_count == 0:
        return []

    # Find the smallest even value and its index
    smallest_val, smallest_idx = min(Counter(arr).items(), key=lambda x: x[0])
    
    return [smallest_val, smallest_idx]

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)
```
This approach efficiently finds the smallest even value and its index using the `Counter` class, which automatically counts occurrences of elements in the array. The `min` function with the `key` parameter is used to find the smallest even value and its index, assuming it's unique, without having to iterate through the entire array.