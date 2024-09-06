```python
def strange_sort_list(lst):
    # Helper function to find the max element in the remaining list
    def max_remainder(L):
        max_so_far = float('-inf')
        for x in L:
            if x > max_so_far:
                max_so_far = x
        return max_so_far

    # Base case: if the list is empty, return it
    if not lst:
        return lst

    # Otherwise, return the minimum value followed by the max of the remaining list
    return [min(lst)] + [max_remainder(lst[1:])] + strange_sort_list(lst[1:])
```

This code defines a recursive function `strange_sort_list()` that takes in a list of integers (`lst`) and sorts it according to the "strange" specification, returning the sorted list. The function uses a helper function, `max_remainder()`, to find the maximum value in a list, which is used in the base case: if the list has only one element, the function returns that element directly, as it is both the minimum and maximum value. Otherwise, the function returns the minimum value, followed by the maximum of the remaining elements, followed by the sorted remainder of the list. This strategy effectively "bubbles" the maximum value up through the sorted list, placing it in the correct position to match the strange sort specification.