```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements present in l. It does so in two steps:
1. First, it removes duplicate elements from l by converting l to a set and then back to a list, leveraging the fact that sets contain only unique elements. This is done using the set() function with the result sorted() to return a sorted list of unique elements.
2. Next, it sorts the elements alphabetically using the built-in sorting function, sorting(l). This ensures that, if the input list contains multiple occurrences of the same element, they will be grouped together in the output list. 

The function header (`def unique(l: list)`) specifies that the function accepts a list and returns a list, and the comment above the function provides a brief description of its behavior. 

This solution is optimized for efficiency and clarity, making it an effective solution to the problem.