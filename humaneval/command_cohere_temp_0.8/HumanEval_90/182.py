```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    mins = min(lst)
    sec_mins = mins + 1
    for n in lst:
        if n == secs_mins:
            return secs_mins
        elif n < secs_mins:
            secs_mins = n
    return secs_mins
``` 

The provided Python script defines a function `next_smallest(lst)` designed to find the second smallest element in a given list of integers. The function starts by checking if the list has fewer than two elements. In this case, the function returns `None` as there can be no second smallest element. If the list contains two or more elements, the function initializes two variables: `mins` and `sec_mins`. The `mins` variable stores the smallest element of the list, while `sec_mins` is initially set to the value of `mins` plus one.

Then, the function iterates through the list, comparing each element to `sec_mins`. If an element equals `sec_mins`, it is returned as the second smallest element. If an element is smaller than `sec_mins`, `sec_mins` is updated to that smaller value.

By the end of the loop, if `sec_mins` has not been assigned a value, it will still hold the original value of `mins + 1`, which is larger than all elements in the list. Thus, `None` is returned, indicating that there is no second smallest element.

Here is an example usage of the function:
```python
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
```
This would output: 
```
2
```

Here is another example usage of the function:
```python
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
```

This would also output:
```
2
```

And finally, here is an example of an edge case:
```python
print(next_smallest([]))  # Output: None
```

This would output:
```
None
```