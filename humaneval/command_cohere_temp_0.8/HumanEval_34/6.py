```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This code defines a function unique which takes a list l as input and returns a sorted list of unique elements from l. Within the function, a set seen is used to keep track of already-seen elements in the list. The function then employs a list comprehension to iterate through the input list, checking if each element is already in the seen set. If it's not, the element is added to the set and also included in the list of unique elements to return. The output is then sorted for easier readability. 

The test cases provided in the original prompt are sufficiency and readability, and this code should pass those tests.