### Unique Elements in a List
#### Problem Description
The function `unique` should return a sorted list of unique elements from the input list.

#### Code Solution

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example Usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation
This code works by first converting the input list into a set, which automatically removes any duplicate elements. Then, it sorts the resulting set in ascending order and returns the result. The `sorted` function is a built-in Python function that returns a new sorted list from the elements of any sequence.