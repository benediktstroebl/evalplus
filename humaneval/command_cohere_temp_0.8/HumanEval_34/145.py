```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, l, which is a list. This function purifies and sorts the list.

First, the function uses the set() function to remove duplicate elements from the list. Set elements are unique by definition, so any duplicate elements in the list will be removed.

Second, the function calls the sort() function to sort the list elements. 

Finally, the function returns the sorted unique list.

This code should be self-contained, as it is stands alone and does not require any imports or external functions to run.  It solves the problem and will pass any tests that expect the output [0, 2, 3, 5, 9, 123] for the given input list ([5, 3, 5, 2, 3, 3, 9, 0, 123]). 

Let me know if I have misunderstood the problem or you would like to troubleshoot output for edge cases!