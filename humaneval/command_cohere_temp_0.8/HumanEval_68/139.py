Here's a Python script that solves the given problem with an efficient approach using `collections.Counter` and `min()` + `next_index`:
```python
from collections import Counter

def pluck(arr):
    if not arr:
        return []
    
    # Count occurrences of each value and find the smallest even value using Counter
    even_values = Counter(val for val in arr if val % 2 == 0)
    smallest_even_val, _ = min(even_values.items(), key=lambda x: x[1])
    
    # Find the index of the smallest even value using next_index
    smallest_index = arr.index(smallest_even_val)
    
    return [smallest_even_val, smallest_index]

# Example Usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)
```

The approach uses the `collections.Counter` to efficiently count the number of occurrences for each value in the array. Even values are filtered and the smallest even value is selected using the `min()` function with a custom key to prioritize items by their count.

The index of the selected value is found using `arr.index()` to fulfill the second part of the challenge. The smallest index where the value is found is selected, fulfilling the secondary requirement.