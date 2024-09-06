```python
def strange_sort_list(lst):
    # Create a temporary list to store the sorted values
    res = []

    # Sort the list based on the criteria mentioned in the prompt
    for i in range(len(lst)):
        # Append the smallest value to the result
        res.append(min(lst[i:]))
        # Remove the smallest value from the remaining list
        lst = lst[i+1:]
        # If the list is empty, break the loop
        if not lst:
            break
    # Append the largest value to the result
    res.append(max(lst))
    return res
```

The function `strange_sort_list()` takes a list of integers (`lst`) as input and sorts it according to the specified criteria. It essentially searches for the smallest value within the remaining list after removing the first element. This process continues iteratively until no elements are left, at which point the largest value is added to the result. The function then returns the final sorted list.

This approach takes advantage of Python's list comprehensions and basic iteration to achieve the desired sorting algorithm. It's important to note, however, that this method has a time complexity of O(n^2) due to the nested loops, which may not be efficient for very large input lists. But it effectively solves the problem as requested in the prompt.