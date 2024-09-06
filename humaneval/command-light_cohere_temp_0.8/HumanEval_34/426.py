Here's a self-contained Python function that sorts and returns unique elements from a list in a markdown-formatted code block:
```python
# Function to get unique elements from a list
def unique(lst):
    # Sort the list first
    lst.sort()
    unique = list(set(lst))
    # Return the unique list
    return unique
```

The function unique takes a list as input and first sorts the list using the sort() method. Then, it converts the list to a set and creates a new list with unique elements using the set() method. Finally, it returns the unique list containing only the unique elements from the original list.