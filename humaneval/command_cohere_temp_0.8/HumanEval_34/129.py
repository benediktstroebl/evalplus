```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, l, which is a list. This function works by first converting the list into a set, which automatically removes any duplicate elements. Then, the set is converted back into a list, and the elements are sorted in ascending order. Finally, the function returns the sorted unique list.

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This would output the following:
```
[0, 2, 3, 5, 9, 123]
```

The function unique() returns a list of sorted, unique elements from the input list, as specified in the problem statement. Feel free to test it with different input lists to verify its functionality further. Let me know if you would like me to explain any part of the code in more detail.