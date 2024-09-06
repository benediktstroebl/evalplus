```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
        result.append(max(lst))
        lst = [x for x in lst if x != max(lst)]
    return result
```

The code starts with creating an empty list called `result` which will store the sorted list in the end. It then enters a while loop that continues until the input list `lst` is empty, meaning that all elements have been processed. In each iteration of the loop, it appends the minimum element to the `result` list and removes it from the input list. It keeps doing this until it reaches a single element in the list, at which point it adds the maximum to the result and removes it from the list. The loop will eventually reach an empty list and therefore will stop. Finally, the function returns the `result` list containing the elements in the required "strange" order. 

Such sorting creates a kind of "zig-zag" pattern, starting from the left with the minimum value, then the highest, then the second lowest, and so on. This is somewhat reminiscent of the selection sort algorithm, but significantly less efficient, especially for larger lists. 

This solution has a time complexity of `O(n^(2))`, making it inefficient for large lists. But it clearly demonstrates the requested sorting pattern. 

This approach also results in a neat and concise implementation, using only basic Python and list manipulation capabilities.  This makes it an excellent educational example for Python noobs, showing the power of Python to solve real problems with simple functions.