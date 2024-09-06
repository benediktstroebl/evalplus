```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list comprehension to efficiently filter out duplicate elements and ensure uniqueness. The 'not seen.add(element)' expression checks whether an element is about to be added to the set, effectively validating whether it's a unique element. 

The function returns a sorted list of unique elements, as advertised. 

It passes the following test:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
``` 

As evidenced by the output above, it accurately solves the problem.