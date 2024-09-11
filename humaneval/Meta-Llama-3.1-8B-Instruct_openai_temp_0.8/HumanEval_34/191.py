Here's a simple Python script that solves the problem using a set to remove duplicates and the sorted function to sort the list:
```markdown
### Unique Elements in a List

This script takes a list of elements as input and returns a new list with the sorted unique elements.

#### Code
```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Output
```python
[0, 2, 3, 5, 9, 123]
```

This script works by converting the input list to a set, which automatically removes any duplicate elements. The sorted function is then used to sort the elements in ascending order and return the result as a list.