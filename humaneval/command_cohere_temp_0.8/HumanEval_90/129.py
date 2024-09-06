```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that solves the problem as stated in the provided code block. It sorts the input list of integers, then checks if the length of the list is less than 2. If the list is empty or contains only one element, it returns `None` to represent the absence of a second smallest value. However, if there are two or more elements in the list, it returns the second element (the second smallest value) using indexing on the sorted list.

Here is a markdown code block showing an example application of the function on the input `[1, 2, 3, 4, 5]` to return its second smallest value:
```python
>> lst = [1, 2, 3, 4, 5]
>> next_smallest(lst)
2
```

The function successfully identifies `2` as the second smallest value in the given list.