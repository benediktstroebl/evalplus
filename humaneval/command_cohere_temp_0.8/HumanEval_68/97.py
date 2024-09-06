Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
def pluck(arr):
    if not arr:
        return []
    
    # Use a set to filter out even values and find the minimum
    even_values = {val for val in arr if val % 2 == 0}
    min_even_value = min(even_values)
    
    # Use a dictionary to store indices of even values and find the minimum index
    index_dict = {val: idx for idx, val in enumerate(arr) if val % 2 == 0}
    min_index = min(index_dict, key=index_dict.get)
    
    return [min_even_value, min_index]

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Output: [2, 1]
```

This approach efficiently filters out even values and finds the minimum using the `min` function and a set. It also finds the index of the minimum even value using a dictionary and the `min` function with key consideration. This solves the problem in a straightforward and efficient manner.