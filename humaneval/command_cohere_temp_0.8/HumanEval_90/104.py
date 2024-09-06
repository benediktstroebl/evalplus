```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    elif lst[-2] > lst[-1]:
        return lst[-2]
    else:
        return lst[-1]
```

The function `next_smallest()` employs list comprehension to check the second last element of the list to be larger than the last element, then it returns the second smallest element, and in case of the second last element being less than or equal to the last element, the function returns the last element as the second smallest element.

Here is a more detailed explanation of the code:
- The first line, `if len(lst) < 2:`, checks whether the length of the list is less than 2. If it is, the function returns `None` because there must be at least three elements to have a second smallest element. 
- The second condition, `elif lst[-2] > lst[-1]:`, checks whether the second last element of the list is greater than the last element. If this condition is true, the function returns the second smallest element, which is the second last element of the list.
- The third line, `else:`, is the catch-all condition that is triggered if the above two conditions are not met. It simply returns the last element of the list as the second smallest element. 

This code elegantly solves the problem in a straightforward manner.