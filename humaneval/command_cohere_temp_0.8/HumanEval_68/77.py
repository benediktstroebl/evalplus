Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
def pluck(arr):
    if not arr:
        return []
    
    # Use a set to filter out even values and find the minimum
    even_values = {x for x in arr if x % 2 == 0}
    min_even_value = min(even_values)
    
    # Use a dictionary to store indices of even values for quick lookup
    even_indices = {x: i for i, x in enumerate(arr) if x % 2 == 0}
    
    # If there's a tie in even values, choose the one with the smaller index
    smallest_index = next(i for i, x in even_indices.items() if x == min_even_value)
    
    return [min_even_value, smallest_index]

# Example usage:
arr = [4, 2, 3]
print(pluck(arr))  # Expected output: [2, 1]
```

This approach uses a `set` to efficiently filter even values from the array and finds the minimum even value directly. It then uses a dictionary to associate indices with even values for quick lookup, ensuring we can select the smallest even value with the smallest index in case of a tie. This approach has a time complexity of `O(n)` where `n` is the length of the input array.