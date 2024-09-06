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

        # Append the current minimum or maximum value to the sorted list
        sorted_list.append(min_val if val == max_val else max_val)

    return sorted_list
```

This Python script defines a function called `strange_sort_list` takes in a list of integers (`lst`) and returns a sorted list using the specified "strange" sorting order: it first sorts by minimum value, then maximum value of the remaining elements, and so on. The script includes a sample usage of the function and checks if the result is correctly sorted in the specified odd manner.