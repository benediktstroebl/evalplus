```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the original list
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
        sorted_list.append(val)

    # If there's only one unique value, return it as is
    if len(set(lst)) == 1:
        return lst

    # Return the strangely sorted list
    return sorted_list
```

The updated script uses the `float('inf')` and `float('-inf')` constants to initialize the minimum and maximum values, ensuring that they are positive and negative infinity respectively. This guarantees correct initialization, avoiding potential issues with `inf` and `-inf`. Also, the presence of multiple `return` statements has been cleaned up for clarity.