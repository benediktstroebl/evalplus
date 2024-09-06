```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Ensure that empty lists return an empty list
    if not lst:
        return []

    for val in lst:
        # Update minimum and maximum values
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the value to the sorted list in the correct order
        if val == min_val:
            sorted_list.append(max_val)
        else:
            sorted_list.append(min_val)
    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input and returns a sorted list following the specified strange ordering: it first sorts by minimum value, then maximum value of the remaining elements, then minimum of the remaining, and so on. The script includes an example usage and a blank line between the function and the example usage for better readability. 

The function initializes min_val and max_val to positive and negative infinity respectively, ensuring that the loop can correctly identify the first encountered minimum and maximum values. It also initializes an empty list called sorted_list, which will store the elements in the desired strange order. The loop iterates through the input list, updating the min_val and max_val as necessary and appending elements to the sorted_list with the appropriate logic to maintain the strange sorting pattern.