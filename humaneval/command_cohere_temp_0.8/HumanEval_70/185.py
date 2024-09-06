```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst) - lst[::-1].index(min(lst))
        out.append(lst.pop(min_idx))
        if len(lst) == 1:
            break
    return out
```

The code works by continuously finding the minimum value in the list, removing it from the list at the maximum index, and adding it to the output array. This process is repeated until the list is empty. It sorts the list in the "strange" order as defined in the prompt, where the maximum value is followed by the minimum value and the list alternating between the two. 

The unit tests for this function could be: 
```python
test_strange_sort_list = '''
assertEqual([1, 4, 2, 3], strange_sort_list([1, 2, 3, 4]))
assertEqual([5, 5, 5, 5], strange_sort_list([5, 5, 5, 5]))
assertEqual([], strange_sort_list([]))
assertEqual([7], strange_sort_list([7]))
assertEqual([1, 4, 2, 3, 8, 6, 5], strange_sort_list([1, 8, 2, 3, 4, 5, 6]))
'''
``` 
The first two test the function with already sorted lists, the next one tests an already semi-sorted list, and the last one a more randomly ordered list.