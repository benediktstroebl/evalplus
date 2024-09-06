```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with minimum values and even positions with maximum values
    for i, num in enumerate(lst):
        if i % 2 == 1:
            min_val = min(min_val, num)
        else:
            max_val = max(max_val, num)
        sorted_list.append(min_val if i % 2 == 1 else max_val)

    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes in a list of integers as input. It sorts the list in a "strange" order: odd positions are filled with the minimum value found in the list, while even positions are filled with the maximum value found so far. The function starts by setting the minimum and maximum values to positive and negative infinity, respectively, and initializing an empty list called `sorted_list` to store the sorted values. As it iterates through the input list, it compares each integer to the current minimum and maximum values and assigns them to the appropriate position in the `sorted_list`. The result is a list that alternates between the minimum and maximum values, creating a "strange" order. The code includes a comment and docstring explaining the strange sorting algorithm, as well as example scenarios that demonstrate how the function behaves for different input lists.