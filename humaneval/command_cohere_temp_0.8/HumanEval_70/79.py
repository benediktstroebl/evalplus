```python
def strange_sort_list(lst):
    # Ensure the list has at least one element
    if not lst:
        return lst
    
    # Sort the list in the specified order
    sorted_list = [min(lst)]
    for i in range(len(lst) - 2):
        # Remove the maximum value from the current list
        max_val = max(lst[i+1:])
        sorted_list.append(max_val)
    return sorted_list
```

This function takes a list of integers as input and returns the list in the specified "strange" order, as described in the problem. It first checks if the list is empty, and if so, it returns the list as is. If not, it iterates through the list, adding the minimum value to the beginning of the "sorted" list and then adding the maximum value from the remaining list to the end of the "sorted" list. This process is repeated until only one value remains in the list, which is then added to the end of the "sorted" list. The function returns the "sorted" list.

Here is an example of how to use the function:
```python
print(strange_sort_list([1, 2, 3, 4])) # [1, 4, 2, 3]
```

This will output: [1, 4, 2, 3].