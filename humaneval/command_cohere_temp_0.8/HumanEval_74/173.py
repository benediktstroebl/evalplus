```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else max(set(lst1 + lst2), key=len)
```

The code uses a simple approach to solve the problem. In this approach, it checks whether the length of the two lists is the same; if they are the same, it returns the first list; otherwise, it returns the list with less characters. Here the `max` function with `key` argument is used to return the list with minimum characters.

Also, the function uses the `set` method to eliminate the duplicate strings so that any duplicate strings in both lists are considered only once.

Note: The approach assumes that each string in the list is different. 

This approach doesn't require any external libraries; it works with standard Python functionality. You can test this code with the provided test cases or more cases to ensure its reliability. UME DEVINUE EYE CATCHER!!